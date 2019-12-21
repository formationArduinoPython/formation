from microbit import *

R0 = 1000
Ualim = 3.13
temperature = 100
temperature_liste, Requiv_liste = [], []

print("#T;Requiv")

while True:
    if button_a.is_pressed():
        while temperature > 30 : 
            # acquisition température
            valeurAnaTMP36 = pin0.read_analog()
            tensionA0 = valeurAnaTMP36*Ualim/1023
            temperature = (tensionA0 - 0.5)*100
        
            # acquisition Requiv
            valeurAnaUequiv = pin2.read_analog()
            Uequiv = valeurAnaUequiv*Ualim/1023
            Requiv = R0*Uequiv/(Ualim - Uequiv)
  
            # affichage
            print(temperature,";",Requiv)
            
            # temporisation
            sleep(5000)
            
            # sortie de secours
            if button_b.is_pressed():
                print("stop")
                break
