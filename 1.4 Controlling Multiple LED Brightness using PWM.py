from machine import Pin, PWM
from time import sleep

led_RD = PWM(Pin(6))
led_GN = PWM(Pin(7))
led_BU = PWM(Pin(8))
led_RD.freq(1000)
led_GN.freq(1000)
led_BU.freq(1000)

while True:
    for duty in range(65025):
        led_RD.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        led_RD.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025):
        led_GN.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        led_GN.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025):
        led_BU.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        led_BU.duty_u16(duty)
        sleep(0.0001)
