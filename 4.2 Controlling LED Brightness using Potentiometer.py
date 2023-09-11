from machine import ADC,Pin
from time import sleep

led_RD = Pin(6,Pin.OUT)

POT = ADC(26)

while True:
    
    print(POT.read_u16())
    
    if POT.read_u16() > 20000 and POT.read_u16() < 40000:
        led_RD.value(1)
        sleep(0.1)
        
    else:
        led_RD.value(0)
        sleep(0.1)
