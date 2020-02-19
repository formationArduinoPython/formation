from microbit import *
import utime

file = open("datas.csv", "w")
file.write("#temps;charge\n")
t = 0
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
            print(t, ";", val)
            file.write(str(t))
            file.write(";")
            file.write(str(val))
            file.write("\n")
            
    if button_b.is_pressed(): 
        pin8.write_digital(0)
        sleep(1000)
        file.close()
        break
