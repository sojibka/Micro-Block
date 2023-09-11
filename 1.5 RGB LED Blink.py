from machine import Pin
from utime import sleep

led_R = Pin(2, Pin.OUT)
led_G = Pin(3, Pin.OUT)
led_B = Pin(4, Pin.OUT)

while True:
    
    led_R.value(1)
    led_G.value(0)
    led_B.value(0)  
    sleep(0.5)
    
    led_R.value(0)
    led_G.value(1)
    led_B.value(0)  
    sleep(0.5)
    
    led_R.value(0)
    led_G.value(0)
    led_B.value(1)  
    sleep(0.5)
    
    print("End of Loop")
    
    led_R.value(0)
    led_G.value(0)
    led_B.value(0)  
    sleep(0.5)
