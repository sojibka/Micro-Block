from machine import Pin, PWM
from time import sleep

PB_1 = Pin(10, Pin.IN)
PB_2 = Pin(11, Pin.IN)
PB_3 = Pin(12, Pin.IN)
PB_4 = Pin(13, Pin.IN)
buzzer = PWM(Pin(28))

def DO(time, vol):
    buzzer.freq(1046)  # Set the frequency to 1046 Hz (Note: C6)
    buzzer.duty_u16(vol)  # Set the duty cycle to control the volume
    sleep(time)
    buzzer.duty_u16(0)  # Turn off the buzzer after the specified time

def RE(time, vol):    
    buzzer.freq(1175)  # Set the frequency to 1175 Hz (Note: D6)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

def MI(time, vol):          
    buzzer.freq(1318)  # Set the frequency to 1318 Hz (Note: E6)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

def FA(time, vol):     
    buzzer.freq(1397)  # Set the frequency to 1397 Hz (Note: F6)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

while True:
    if PB_1.value() == True:
        print("Button 1 Pressed")
        DO(0.2, 32768)  # Calling DO function with time=0.2 seconds and vol=32768 (mid-level volume)
    elif PB_2.value() == True:
        print("Button 2 Pressed")
        RE(0.2, 32768)  # Calling RE function with time=0.2 seconds and vol=32768 (mid-level volume)
    elif PB_3.value() == True:
        print("Button 3 Pressed")
        MI(0.2, 32768)  # Calling MI function with time=0.2 seconds and vol=32768 (mid-level volume)
    elif PB_4.value() == True:
        print("Button 4 Pressed")
        FA(0.2, 32768)  # Calling FA function with time=0.2 seconds and vol=32768 (mid-level volume)
    else:
        PB_1.value(0)  # Set PB_1 to low (False)
        PB_2.value(0)  # Set PB_2 to low (False)
        PB_3.value(0)  # Set PB_3 to low (False)
        PB_4.value(0)  # Set PB_4 to low (False)

