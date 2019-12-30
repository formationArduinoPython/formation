from microbit import *

print('bouton A : debut des mesures    bouton B : fin')

temperature = 100
Ualim = 3.13
R0 = 1000
n = 0 # un compteur pour enregistrement dans fichier
while True:
    if button_a.is_pressed():
        with open('data.csv', "w") as f:
            f.write('T;Requiv\n')
            while temperature > 30:
                """
                acquisition de la température
                """
                valeurAnaTMP36 = pin0.read_analog()
                tensionA0 = valeurAnaTMP36 *Ualim/1023
                temperature = (tensionA0 - 0.5)*100
                """
                acquisition de Requivalente
                """
                valeurAnaUequiv = pin2.read_analog()
                Uequiv = valeurAnaUequiv*Ualim/1023
                Requiv = R0*Uequiv/(Ualim-Uequiv)
                """
                affichage
                """
                print(temperature,";",Requiv)
                """
                écriture dans fichier toutes les 3 mesures
                """
                if n % 3 == 0: 
                    f.write('{};{}\n'.format(temperature, Requiv))
                n+=1
                """
                temporisation
                """
                sleep(5000)
                """
                sortie de secours
                """
                if button_b.is_pressed():
                    print('arret des mesures')
                    break

