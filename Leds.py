import RPi.GPIO as GPIO
from gpiozero import LEDBoard, Button

leds = LEDBoards(5, 7, 11, 13)

def num(i):
    switcher = {
        0: led.off(),
        1: led.on(3),
        2: led.on(2),
        3: led.on(2, 3),
        4: led.on(1),
        5: led.on(1, 3),
        6: led.on(1, 2),
        7: led.on(1, 2, 3),
        8: led.on(0),
        9: led.on(0, 3)
    }

button(3)

led.off()
while true:
    for i in range(10):
        button.wait_for_press()
        led.off()
        num(i)
