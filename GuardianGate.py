import cv2
import mediapipe as mp
import RPi.GPIO as GPIO
import time
from gpiozero import LED, Button, Buzzer

# ==================== GPIO / PIN SETUP ====================
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_green = LED(23)      # green LED -> system idle / safe
led_red    = LED(24)     # red LED   -> fault / intrusion
button     = Button(22)  # emergency stop button
buzzer     = Buzzer(27)  # alarm buzzer

SERVO_PIN = 13
TRIG = 16
ECHO = 17

GPIO.setup(TRIG, GPIO.OUT)        # sends pulse to ultrasonic sensor
GPIO.setup(ECHO, GPIO.IN)         # receives pulse back
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)     # 50Hz standard for servos
pwm.start(0)


# ==================== SERVO HELPERS ====================
def angle_to_duty(angle):
    return 2 + (angle / 18)

def smooth_move(start_angle, end_angle, step=1, delay_time=0.02):
    """Moves servo gradually instead of snapping - this is the 'motion profiling'."""
    if start_angle < end_angle:
        angle_range = range(start_angle, end_angle + 1, step)
    else:
        angle_range = range(start_angle, end_angle - 1, -step)

    for angle in angle_range:
        pwm.ChangeDutyCycle(angle_to_duty(angle))
        time.sleep(delay_time)

def servo_close():
    smooth_move(90, 0, step=1, delay_time=0.02)
    pwm.ChangeDutyCycle(0)   # stop holding torque once closed

def servo_open():
    smooth_move(0, 90, step=1, delay_time=0.02)


# ==================== ULTRASONIC HELPER ====================
def get_distance(timeout=0.05):
    """
    Returns distance in cm, or None if sensor timed out
    (prevents the program from freezing forever if sensor misbehaves)
    """
    GPIO.output(TRIG, 0)
    time.sleep(0.05)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    start_wait = time.time()
    while GPIO.input(ECHO) == 0:
        if time.time() - start_wait > timeout:
            return None              # sensor didn't respond, give up safely
    start_time = time.time()

    start_wait = time.time()
    while GPIO.input(ECHO) == 1:
        if time.time() - start_wait > timeout:
            return None
    end_time = time.time()

    travel_time = end_time - start_time
    distance = (travel_time * 34300) / 2   # speed of sound / 2 (round trip)
    return distance


# ==================== HAND GESTURE HELPER ====================
mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils

def is_hand_open(hand_landmarks):
    tips  = [8, 12, 16, 20]
    bases = [6, 10, 14, 18]
    fingers_up = 0
    for tip, base in zip(tips, bases):
        tip_y  = hand_landmarks.landmark[tip].y
        base_y = hand_landmarks.landmark[base].y
        if tip_y < base_y:
            fingers_up += 1
    return fingers_up == 4


# ==================== STATE MACHINE VARIABLES ====================
current_state  = "IDLE"
open_counter   = 0
CONFIRM_FRAMES = 5          # need 5 consecutive open-hand frames to confirm (debounce)
SAFE_DISTANCE  = 50         # cm - path considered clear if distance > this

actuating_start_time = None
fault_start_time      = None


# ==================== CAMERA SETUP ====================
url = "http://100.121.120.166:8080/video"
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("ERROR: Cannot connect to IP Webcam stream")
    exit()


# ==================== MAIN LOOP (everything happens here, ONE loop) ====================
servo_close()

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
) as hands:

    try:
        while True:

            # ---------- 1. Emergency stop check (works from ANY state) ----------
            if button.is_pressed:
                current_state = "FAULT"
                led_red.on()
                buzzer.on()
                servo_close()
                fault_start_time = time.time()

            # ---------- 2. Read camera frame ----------
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame, retrying...")
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            hand_open_now = False   # default: assume closed/no hand this frame

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    hand_open_now = is_hand_open(hand_landmarks)

            # ---------- 3. Read ultrasonic sensor ----------
            dist = get_distance()
            path_clear = (dist is not None) and (dist > SAFE_DISTANCE)

            # ---------- 4. STATE MACHINE ----------
            if current_state == "IDLE":
                led_green.on()
                led_red.off()
                buzzer.off()

                if hand_open_now:
                    open_counter += 1
                else:
                    open_counter = 0   # reset only when hand is NOT open

                if open_counter >= CONFIRM_FRAMES:
                    current_state = "ARMED"
                    open_counter = 0
                    print("Gesture confirmed -> ARMED")

            elif current_state == "ARMED":
                # gesture confirmed, now verify path before moving
                if path_clear:
                    current_state = "VERIFYING"
                    print("Path looks clear")
                else:
                    print("Path is blocked")
                    # stays in ARMED, keeps checking

            elif current_state == "VERIFYING":
                # double-check before actually moving (extra safety)
                if path_clear:
                    current_state = "ACTUATING"
                    servo_open()                     # smooth open motion
                    actuating_start_time = time.time()
                    print("Opening gate ")
                else:
                    current_state = "FAULT"
                    fault_start_time = time.time()
                    print("Obstruction detected during verify")

            elif current_state == "ACTUATING":
                led_green.on()
                # check continuously while gate is open for intrusion
                if not path_clear:
                    current_state = "FAULT"
                    fault_start_time = time.time()
                    print("Intrusion while open")
                elif time.time() - actuating_start_time > 5:   # stay open 5 sec
                    servo_close()
                    current_state = "IDLE"
                    print("Auto-closing ")

            elif current_state == "FAULT":
                led_green.off()
                led_red.on()
                buzzer.on()

                if time.time() - fault_start_time > 5:   # recover after 5 sec
                    buzzer.off()
                    led_red.off()
                    current_state = "IDLE"
                    print("Fault cleared")

            # ---------- 5. Show status on screen ----------
            dist_text = f"{dist:.1f} cm" if dist is not None else "no reading"
            
            print(
                f"\rState={current_state} | Distance={dist_text} | HandOpen={hand_open_now}",
                end=""
            )

    except KeyboardInterrupt:
        print("\nComplete")

# ==================== CLEANUP ====================
cap.release()
pwm.stop()
GPIO.cleanup()
