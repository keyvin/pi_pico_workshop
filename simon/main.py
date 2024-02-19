import time
import machine
import button
import buzzer
import led

def stop_all():
    global stoppable
    for i in stoppable:
        i.stop()


def button1_callback():
    print("Button 1")
    stop_all()
    
def button2_callback():
    print("Button 2")
    stop_all()
        
def button3_callback():
    print("Button 3")
    stop_all()



buzz = buzzer.Buzzer(16,300)
b1 = button.Button(0, button1_callback, 20, 50, True) 
b2 = button.Button(1, button2_callback, 20, 50, True) 
b3 = button.Button(2, button3_callback, 20, 50, True) 
r_led = led.LED(19)
y_led = led.LED(18)
g_led = led.LED(17)

stoppable = [buzz, r_led,y_led,g_led]




keys = [[r_led, 400], [y_led, 600], [g_led,800]]

sequence = [1,0,1,2]

def show_sequence(sequence):
    global buzz
    for i in sequence:
        keys[i][0].turn_on(1000)
        buzz.start_buzz(keys[i][1],1000)
        print(keys[i][1])
        time.sleep(1)
        keys[i][0].stop()
        buzz.stop()

show_sequence(sequence)

num_presses = 0
press = 0
while True:
    buzz.check()
    r_led.check()
    y_led.check()
    g_led.check()
    if b1.check():
        press = 1
    if b2.check():
        press = 2
    if b3.check():
        press = 3
    if press > 0:
        press = press -1
        if num_presses >= len(sequence):
            num_presses = 0
            
        if sequence[num_presses] == press:
            num_presses = num_presses + 1
            keys[press][0].turn_on(1000)
            buzz.start_buzz(keys[press][1], 1000)
        else:
            stop_all()
            show_sequence(sequence)
            num_presses = 0
    press = 0  
    
    
        
    
        
    