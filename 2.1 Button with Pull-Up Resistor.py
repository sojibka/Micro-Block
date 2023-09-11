from machine import Pin
from time import sleep

print('READY TO TEST BUTTON')

PB_1 = Pin(10, Pin.IN)  # 10 number pin is input
PB_2 = Pin(11, Pin.IN)  # 11 number pin is input
PB_3 = Pin(12, Pin.IN)  # 12 number pin is input
PB_4 = Pin(13, Pin.IN)  # 13 number pin is input

while True:
        
    if PB_1.value() == 1:       # if push_button pressed
        print('Push Button 1 is Pressed')
        sleep(0.2)
        
    if PB_2.value() == 1: 
        print('Push Button 2 is Pressed')
        sleep(0.2)
        
    if PB_3.value() == 1:
        print('Push Button 3 is Pressed')
        sleep(0.2)
        
    if PB_4.value() == 1:
        print('Push Button 4 is Pressed')
        sleep(0.2)
    
    else:                        # if push_button not pressed
        PB_1.value(0)            # led will turn OFF# led will turn OFF
        PB_2.value(0)
        PB_3.value(0)
        PB_4.value(0)
