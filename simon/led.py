import time
import machine
class LED:
    def __init__(self, pin,time_on=1000):
        self.pin = machine.Pin(pin, machine.Pin.OUT)
        self.on = False
        self.ms_turned_on = 0
        self.ms_to_stay_on = time_on
    def turn_on(self, time_to_stay_on):
        self.ms_turned_on = time.ticks_ms()
        self.ms_to_stay_on = time_to_stay_on
        self.pin.value(1)
        self.on=True
    def check(self):
        if time.ticks_diff(time.ticks_ms(), self.ms_turned_on) > self.ms_to_stay_on:
            self.pin.value(0)
            self.on=False
    def stop(self):
        self.pin.value(0)
        self.on=False