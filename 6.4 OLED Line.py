from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.line(0, 0, 127, 63, 1)
oled.hline(20,30,60,1)
oled.vline(30, 0, 64, 1)
oled.show()
