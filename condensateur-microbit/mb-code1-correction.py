from microbit import *

t = 0
print("#t(ms);charge")
pin8.write_digital(0)
sleep(300)

while True : 
    if button_a.is_pressed(): 
        pin8.write_digital(1)
        t0 = running_time()
        while (t <= 300): 
            t = running_time()-t0
            val = pin0.read_analog()
            print(t, ";", val)
    
    if button_b.is_pressed(): 
        pin8.write_digital(0)
        sleep(1000)
        break
