from machine import Pin
from utime import sleep

led_RD = Pin(2, Pin.OUT)
led_GN = Pin(3, Pin.OUT)
led_BU = Pin(4, Pin.OUT)

time = 0.5

while True:
    
    led_RD.value(1)
    led_GN.value(0)
    led_BU.value(0)  
    sleep(time)
    
    led_RD.value(0)
    led_GN.value(1)
    led_BU.value(0)  
    sleep(time)
    
    led_RD.value(0)
    led_GN.value(0)
    led_BU.value(1)  
    sleep(time)
    
    led_RD.value(1)
    led_GN.value(1)
    led_BU.value(0)  
    sleep(time)
    
    led_RD.value(1)
    led_GN.value(0)
    led_BU.value(1)  
    sleep(time)
    
    led_RD.value(0)
    led_GN.value(1)
    led_BU.value(1)  
    sleep(time)
    
    led_RD.value(1)
    led_GN.value(1)
    led_BU.value(1)  
    sleep(time)
    
    print("End of Loop")
    
    led_RD.value(0)
    led_GN.value(0)
    led_BU.value(0)  
    sleep(time)
