from machine import Pin
import time

p0 = Pin(1, Pin.OUT)
p2 = Pin(0, Pin.IN, Pin.PULL_UP)

#pullup and pulldown resistors
#active logic high vs logic low. 

p0.value(0)

#initial state of the LED
state = False
#loop forever
while True: 
    if p2.value() == False: #Button pressed?
        time.sleep_ms(20) #software debounce
        state = not state #flip state
        p0.value(state) #change LED PIN
        while not p2.value() == True: #wait for release
            pass
        time.sleep_ms(10) #software debounce

