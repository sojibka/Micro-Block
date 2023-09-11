from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.rect(32, 48, 16, 4, 1)
oled.show()

#  oled.fill_rect(32, 48, 16, 4, 1)
#  oled.show()
