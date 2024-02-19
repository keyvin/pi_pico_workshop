import machine
import time
from machine import Pin

DEBOUNCE = 30
PRESS = 300
BOARD_PULL_UP=True

class Button():
    def __init__(self, pin, push_function, debounce_ms=DEBOUNCE, long_press_ms=PRESS, pullup=BOARD_PULL_UP):
        if pullup == True:
            self.button = [machine.Pin(pin,Pin.IN, Pin.PULL_UP), 1,0]
            self.active = 0
        else:
            self.button = [machine.Pin(pin,Pin.IN, Pin.PULL_DOWN),0,0]
            self.active = 1
        self.push_function = push_function
        self.debounce_ms = debounce_ms
        self.long_press_ms = long_press_ms
    
    def check(self):
        global MUTE
        curr_ms = time.ticks_ms()
        current = self.button[0].value()
        time_diff = time.ticks_diff(curr_ms, self.button[2])
    #if button state does not match last state
        if current != self.button[1]:
            if current != self.active:     #if transitioning from pressed to not press
                if time_diff < self.debounce_ms:     #software debounce
                    pass  #not steady yet
                elif time_diff < self.long_press_ms:      #held for less than hardpress. 
                    self.button[1] = current      #todo mute beeper for day on softpress
                    self.button[2] = curr_ms
                    MUTE = True
                    print ("Mute")
                else:
                    self.button[1] = current      #hard press, report button press
                    if self.push_function:
                        self.push_function()
                    return(True)
            elif current == self.active:               #transition high to low, mark button held and ms_tick when pressed
                self.button[1] = 0                		#bouncing doesn't matter. 
                self.button[2] = curr_ms 
        return False