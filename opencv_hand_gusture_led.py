import cv2
import mediapipe as mp
import RPi.GPIO as GPIO    # raspberry pi GPIO library

# GPIO setup
LED_PIN = 17               # GPIO pin 17 (physical pin 11)
GPIO.setmode(GPIO.BCM)     # use GPIO numbers not physical pin numbers
GPIO.setup(LED_PIN, GPIO.OUT)  # set pin as output

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def is_hand_open(hand_landmarks):
    # finger tips landmarks
    tips  = [8, 12, 16, 20]   # index, middle, ring, pinky tips
    # finger bases landmarks
    bases = [6, 10, 14, 18]   # index, middle, ring, pinky bases

    fingers_up = 0

    # check each finger if it is up or down
    for tip, base in zip(tips, bases):
        tip_y  = hand_landmarks.landmark[tip].y
        base_y = hand_landmarks.landmark[base].y

        if tip_y < base_y:    # tip above base = finger up
            fingers_up += 1

    if fingers_up == 4:       # all 4 fingers up = hand open
        return True
    else:
        return False           # hand closed
    
url = "http://100.97.165.65:8080/video"    
# open camera
cap = cv2.VideoCapture(url)      # 0 = default raspberry pi camera

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,           # only need 1 hand
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
) as hands:

    while True:
        ret, frame = cap.read()                        # read frame from camera
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # convert BGR to RGB
        results = hands.process(rgb)                   # detect hands

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # draw skeleton on frame
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if is_hand_open(hand_landmarks):
                    # hand open = LED ON
                    GPIO.output(LED_PIN, GPIO.HIGH)    # turn LED on
                    cv2.putText(frame, "OPEN - LED ON", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    # hand closed = LED OFF
                    GPIO.output(LED_PIN, GPIO.LOW)     # turn LED off
                    cv2.putText(frame, "CLOSED - LED OFF", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # show the frame
        cv2.imshow("Hand Detection", frame)

        # press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# cleanup everything when done
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()             # reset all GPIO pins