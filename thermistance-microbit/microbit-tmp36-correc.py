from microbit import *

print("appui sur bouton A pour mesure de temperature")

while True:
    if button_a.is_pressed():
        valeurAnaTMP36 = pin0.read_analog()
        # REM : vérifier tension d'alim (3.26 V) si résultats de température douteux
        tensionA0 = valeurAnaTMP36*3.26/1023    # calcul de la valeur de la tension en volts
        
        temperature = (tensionA0 - 0.5)*100	# calcul de la température
        print("T = ", temperature)              # affichage du résultat
        sleep(1000)                             # temporisation
