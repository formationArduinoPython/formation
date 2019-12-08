from microbit import *

# on initialise la liaison uart via USB (tx et rx à rien)
uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=None, rx=None)

pin8.write_digital(0)
sleep(300)

# tant que la carte ne reçoit rien sur la liaison uart, elle boucle
while uart.any() == False :
    sleep(1)

# et donc ensuite, on est dans l'hyp où elle a reçu qq chose
uart.readline()# on vide le port série en lisant la lettre reçue
t0 = running_time()# initialisation du temps
pin8.write_digital(1)

while True : 
        t = running_time() - t0
        val = pin0.read_analog()
        print(t, ';', val)
