from machine import Pin
from time import sleep

print('READY TO TEST BUTTON')

PB_1 = Pin(10, Pin.IN)
PB_2 = Pin(11, Pin.IN)
PB_3 = Pin(12, Pin.IN)
PB_4 = Pin(13, Pin.IN)

led_R = Pin(2, Pin.OUT)
led_G = Pin(3, Pin.OUT)
led_B = Pin(4, Pin.OUT)
led_RD = Pin(6, Pin.OUT)

while True:
        
    if PB_1.value() == 1:        # if push_button pressed
        led_R.value(1)           # led will turn ON
        print('Push Button 1 is Pressed')
        
    if PB_2.value() == 1: 
        led_G.value(1)
        print('Push Button 2 is Pressed')
        
    if PB_3.value() == 1:
        led_B.value(1)
        print('Push Button 3 is Pressed')
        
    if PB_4.value() == 1:
        led_RD.value(1)
        print('Push Button 4 is Pressed')
    
    else:                        # if push_button not pressed
        led_R.value(0)           # led will turn OFF# led will turn OFF
        led_G.value(0)
        led_B.value(0)
        led_RD.value(0)
