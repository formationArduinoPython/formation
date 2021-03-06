from microbit import *
import utime

t = 0
T,Q=[],[]
print("#t(ms);charge")
pin8.write_digital(0)
sleep(300)

while True: 
    if button_a.is_pressed(): 
        pin8.write_digital(1)
        t0 = utime.ticks_us()
        while (t <= 300000): 
            t = utime.ticks_us() - t0
            val = pin0.read_analog()
            T.append(t);Q.append(val)
            print(t, ";", val)
            
    if button_b.is_pressed(): 
        pin8.write_digital(0)
        sleep(1000)
        print("T = ",T)
        print("Q = ",Q)
        break
