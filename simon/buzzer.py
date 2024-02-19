import time
from machine import PWM
from machine import Pin

BUZZ_ENABLED=True
BUZZ_FREQ = 500
BUZZ_LEN = 1000

class Buzzer():
    def __init__(self, pin, length_ms=BUZZ_LEN):
        self.second_tick_last_turned_on = 0
        self.tone = 0
        self.hz = 0
        self.pwm = PWM(Pin(pin))
        self.length_ms = length_ms
        self.second_tick_last_turned_on = 0
        self.pwm.duty_u16(0)    
        self.on = False
        self.buzzer_start_time_ms = 0
    
    def check(self, overdue=False):        
        time_ms = time.ticks_ms()
        if self.on:
            if time.ticks_diff(time_ms, self.buzzer_start_time_ms) > self.length_ms:
                self.pwm.duty_u16(0)
                self.on = False
        
    def start_buzz(self, tone, length_ms):
        self.on = True
        self.length_ms = length_ms
        self.buzzer_start_time_ms = time.ticks_ms()
        self.pwm.freq(tone)
        self.pwm.duty_u16(32768)
    
    def stop(self):
        self.on = False
        self.pwm.duty_u16(0)
            