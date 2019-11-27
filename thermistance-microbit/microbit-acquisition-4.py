from microbit import *

R0 = 1000
Ualim = 3.13
temperature = 100
temperature_liste, Requiv_liste = [], []
compteur = 0

file = open("donnees2.csv", "w")
file.write("T;Requiv\n")

print("#T;Requiv")

while True:
    if button_a.is_pressed():
        while temperature > 30 :
            sommeTemperatures = 0
            sommeRequiv = 0
            for n in range(20) :
                # acquisition température
                valeurAnaTMP36 = pin0.read_analog()
                tensionA0 = valeurAnaTMP36*Ualim/1023
                temperature = (tensionA0 - 0.5)*100
            
                # acquisition Requiv
                valeurAnaUequiv = pin2.read_analog()
                Uequiv = valeurAnaUequiv*Ualim/1023
                Requiv = R0*Uequiv/(Ualim - Uequiv)

                sommeTemperatures += temperature
                sommeRequiv += Requiv
                sleep(200)
                
            temperature = sommeTemperatures/20
            Requiv = sommeRequiv/20
            
            # affichage, incrémentation du compteur de nbe d'affichages
            print(temperature,";",Requiv)
            compteur+=1

            # écriture dans fichier et listes toutes les 3 acquisitions
            if compteur % 3 == 0 : 
                file.write('{};{}\n'.format(temperature, Requiv))
                temperature_liste.append(temperature)
                Requiv_liste.append(Requiv)
            
            # temporisation
            sleep(1000)
            
            # sortie de secours
            if button_b.is_pressed():
                print("stop")
                break
        
        # affichage des listes
        print('temperature_liste = ',temperature_liste)
        print('Requiv_liste = ',Requiv_liste)
