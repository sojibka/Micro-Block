from machine import Pin, ADC
from time import sleep

photoPIN = 1

def readLight(photoGP):
    photoRes = ADC(Pin(27))
    light = photoRes.read_u16()
    light = round(light/65535*100,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) +"%")
    sleep(0.2)
