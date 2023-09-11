from machine import Pin, ADC
from time import sleep

LDR = ADC(27)  # ADC Pins 26, 27, 28

while True:
    print(LDR.read_u16())
    sleep(0.2)
