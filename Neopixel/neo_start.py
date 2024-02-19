from neopixel import Neopixel
import time
 
numpix = 15
pixels = Neopixel(numpix, 0, 0, "GRB")
green = (0, 255, 0)
blue = (0, 0, 255)
red = (120, 200,50)
color0 = blue
x=0
while True:
    pixels.brightness(x)
    pixels.fill(red)
    pixels.show()
    if x == 0:
        x = 255
    x = x-1
    time.sleep_ms(1)
    