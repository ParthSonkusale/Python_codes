import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Use GPIO numbers (GPIO5, GPIO6) instead of physical pin numbers

TRIG = 5
ECHO = 6

GPIO.setup(TRIG, GPIO.OUT)  # GPIO5 will send signals to the sensor
GPIO.setup(ECHO, GPIO.IN)   # GPIO6 will receive signals from the sensor

while True:
    GPIO.output(TRIG, 0)    # Make sure TRIG is LOW
    time.sleep(0.1)

    GPIO.output(TRIG, 1)    # Send a 10 microsecond trigger pulse
    time.sleep(0.00001)

    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        # Waiting for ECHO to go HIGH
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        # ECHO is HIGH, keep updating end_time
        end_time = time.time()

    travel_time = end_time - start_time

    # Distance = speed × time / 2
    # 34300 cm/s = speed of sound
    # Divide by 2 because sound travels to the object and back
    dist = (travel_time * 34300) / 2

    print("Distance:", round(dist, 2), "cm")