from microbit import *

# on initialise la liaison uart via USB (tx et rx à rien)
uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=None, rx=None)

# décharge du condensateur
pin8.write_digital(0)
sleep(300)

while True : 
    if button_a.is_pressed():
        pin8.write_digital(1) # on attaque la charge
        t0 = running_time() # initialisation du temps
        while True:  # boucle de l'acquisition ; c'est le fichier Python qui décide combien de temps elle va durer
            t = running_time()-t0
            ana = pin0.read_analog()
            print(t, ';', ana)
