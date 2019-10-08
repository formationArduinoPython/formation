from microbit import *

print("appui sur bouton A pour mesure de temperature")

while True:
    if button_a.is_pressed():
        valeurAnaTMP36 = pin0.read_analog()
        tensionA0 = 			# calcul de la valeur de la tension en volts
        temperature = 			# calcul de la température
                                # affichage du résultat
        sleep(1000)                             # temporisation
