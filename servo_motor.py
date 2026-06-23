import RPi.GPIO as GPIO
from time import sleep

# Step 2 & 3: Setup
SERVO_PIN = 18  # change to your GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Step 4: Create PWM object at 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

# Step 5: Helper function - angle to duty cycle
def angle_to_duty(angle):
    return 2 + (angle / 18)

# Step 6: Smooth sweep function
def smooth_move(start_angle, end_angle, step=1, delay_time=0.02):
    if start_angle < end_angle:
        angle_range = range(start_angle, end_angle + 1, step)
    else:
        angle_range = range(start_angle, end_angle - 1, -step)

    for angle in angle_range:
        duty = angle_to_duty(angle)
        pwm.ChangeDutyCycle(duty)
        sleep(delay_time)

try:
    # Move smoothly from 0 to 90 degrees
    smooth_move(0, 90, step=1, delay_time=0.02)

    # Step 7: Hold position briefly
    sleep(1)

    # Optional: move back to 0
    smooth_move(90, 0, step=1, delay_time=0.02)
    sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Step 8: Cleanup
    pwm.stop()
    GPIO.cleanup()