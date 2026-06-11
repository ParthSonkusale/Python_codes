from gpiozero import LED
import time

led_0 = LED(17)
led_1 = LED(27)
led_2 = LED(22)

c = 1
while(c):
    led_0.on()
    led_1.off()
    led_2.off()
    time.sleep(3)
    led_0.on()
    led_1.on()
    led_2.off()
    time.sleep(3)
    led_0.off()
    led_1.off()
    led_2.on()
    time.sleep(3)    
    led_0.off()
    led_1.on()
    led_2.off()
    time.sleep(3)
    led_0.on()
    led_1.off()
    led_2.off()
    time.sleep(3)    

