from machine import Pin, PWM
from time import sleep

led_GN = PWM(Pin(7))
led_GN.freq(1000)

while True:
    for duty in range(65025):
        led_GN.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        led_GN.duty_u16(duty)
        sleep(0.0001)
