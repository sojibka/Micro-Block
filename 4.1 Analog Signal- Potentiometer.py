from machine import Pin, ADC
from time import sleep

POT = ADC(26)  # ADC Pins 26, 27, 28

while True:
    print(POT.read_u16())
    sleep(0.2)
