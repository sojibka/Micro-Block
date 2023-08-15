from machine import Pin
from utime import sleep

led_RD = Pin(6, Pin.OUT)

while True:

    led_RD.value(1)
    sleep(1)
    led_RD.value(0)
    sleep(1)
