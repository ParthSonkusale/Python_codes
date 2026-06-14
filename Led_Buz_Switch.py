from gpiozero import LED, Button, Buzzer

led_1 = LED(17)
led_2 = LED(23)
button = Button(22)
buzzer = Buzzer(27)

cnt = 0
previous_state = False

while True:
    current_state = button.is_pressed

    if current_state and not previous_state:
        cnt += 1

        if cnt % 2 == 0:
            led_1.on()
            led_2.off()
            buzzer.off()
        elif cnt % 3 == 0:
            led_1.off()
            led_2.off()
            buzzer.on()
        else:
            led_1.off()
            led_2.on()
            buzzer.off()

    previous_state = current_state