from machine import Pin, I2C
import ssd1306

#See pinout diagram - i2c0 and i2c1 pins
i2c = I2C(id=1,sda=Pin(14), scl=Pin(15))

display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('Hello, World!', 0, 0, 1)
display.show()