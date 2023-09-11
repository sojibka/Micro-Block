from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)              

x = 64        # ball coordinates on the screen in pixels
y = 0
vx = 1        # ball velocity along x and y in pixels per frame
vy = 1
while True:
    
    oled.fill(0)
    
    oled.fill_rect(x, y, 8, 8, 1)  # Draw a 4x4 pixels ball at (x,y) in white
    oled.show()
    
    x += vx    # Move the ball by adding the velocity vector
    y += vy
