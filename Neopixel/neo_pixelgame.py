from neopixel import Neopixel
import time
import random
import ssd1306
from machine import Pin, I2C

#initialization
i2c = I2C(id=1,sda=Pin(14), scl=Pin(15))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
pixels = Neopixel(12, 0, 0, "GRB")
button_pin_num = 1
button_pin = Pin(button_pin_num, Pin.IN, Pin.PULL_UP)

#colors
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0,0)
off = (0,0,0)
wins =0

delay = initial_delay = 1000
position = 0

last_time = time.ticks_ms()
target = random.randint(0,11) #pick target pixel
pixels.set_pixel(target, red)
display.text("Wins: 0",0,30,1)
display.text("Delay: "+str(delay),0,50,1)
display.show()

#subroutine to blink the lights
def flash(color):
    for i in range(0,3):
        pixels.fill(color)
        pixels.show()
        time.sleep(.5)
        pixels.fill(off)
        pixels.show()
        time.sleep(.5)

while True:
    #sleep will not work for this - we will miss button presses.
    #compare elapsed time.
    if  time.ticks_ms() - last_time > delay or time.ticks_ms() < last_time:
        pixels.set_pixel(position, off) #turn off led
        position = position + 1 #advance position
        if position > 11: #wrap if needed
             position = 0
        if target==position: #if overlap (correct), indicate it with color
            pixels.set_pixel(position, (255,0,255))
        else:
            pixels.set_pixel(position, blue) #refresh target and 
            pixels.set_pixel(target, red)    #position
        last_time = time.ticks_ms()          #set next refresh
        pixels.show()                        #show strip
    if button_pin.value() == False:          #check button
        if position == target:       #win!            
            delay = delay *.9            
            flash(green)
            wins = wins +1
        else:                       #lose :(
            delay = intial_delay
            flash(red)
            wins =0 
        target = random.randint(0,11)   #pick new target
        position =0        
        pixels.set_pixel(target, red)    #set position and target
        pixels.set_pixel(position, blue)
        
        display.fill(0)                     #redraw screen  
        display.text("Wins:"+str(wins),0,30,1)
        display.text("Delay: "+str(delay),0,50,1)
        display.show()
        last_time = time.ticks_ms()        #reset time
        
