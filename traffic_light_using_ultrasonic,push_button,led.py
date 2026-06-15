from gpiozero import LED, Button, Buzzer
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led_r = LED(17)
led_y = LED(27)
led_g = LED(22)

P_Butt = Button(23)
Buzz = Buzzer(24)

TRIG = 5
ECHO = 6

start_time = 0
end_time = 0

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:

        # Trigger ultrasonic pulse
        GPIO.output(TRIG, False)
        time.sleep(0.05)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Wait for echo start
        timeout = time.time() + 0.05
        while GPIO.input(ECHO) == 0:
            start_time = time.time()
            if time.time() > timeout:
                break

        # Wait for echo end
        timeout = time.time() + 0.05
        while GPIO.input(ECHO) == 1:
            end_time = time.time()
            if time.time() > timeout:
                break

        travel_time = end_time - start_time
        dist = (travel_time * 34300) / 2
        print("start =" , start_time )
        print("end =" , end_time )
        print(f"Distance = {dist:.2f} cm")

        # Pedestrian crossing
        if P_Butt.is_pressed:

            print("Pedestrian Button Pressed")

            led_r.on()
            led_y.off()
            led_g.off()

            Buzz.on()
            time.sleep(8)
            Buzz.off()

        # Vehicle detected
        elif dist <= 20:

            print("Vehicle Detected")

            led_r.off()
            led_y.off()
            led_g.on()

            Buzz.off()
            time.sleep(3)

        # Normal traffic cycle
        else:

            Buzz.off()

            # Red
            led_r.on()
            led_y.off()
            led_g.off()
            time.sleep(3)

            # Red + Yellow
            led_r.on()
            led_y.on()
            led_g.off()
            time.sleep(1)

            # Green
            led_r.off()
            led_y.off()
            led_g.on()
            time.sleep(3)

            # Yellow
            led_r.off()
            led_y.on()
            led_g.off()
            time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Stopped")

finally:
    GPIO.cleanup()