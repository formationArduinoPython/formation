from pyfirmata import Arduino, util
import time

# modifiez le nom du port (lisible en bas à droite sur l'IDE Arduino)
carte = Arduino("/dev/ttyACM0", baudrate = 57600)


it = util.Iterator(carte)
it.start()

########################
# définition des broches
########################
A0 = carte.get_pin("a:0:i")#analog 0 input
D7 = carte.get_pin("d:7:o")# digital 7 output
# broche A0 ; on veut lire la valeur ana et le temps

#################################
# démarrage commandé par un input
#################################
demarrage = input("Quand vous voulez... ")

#######################
# démarrage
#######################
D7.write(0) # on décharge le condensateur au cas où...
time.sleep(1) # pendant 1 seconde
print("START")
print("#temps;valeur")
time.sleep(0.2) # 0.2 s avant de lancer l'acquisition



######################
# boucle d'acquisition
######################

# un booléen pour rentrer ds la boucle
flag = False
# listes de données acquises
T,Q=[],[]
# temps max pour l'acquisition (ms) à déterminer en fonction de R et C
tmax = 300

# allumage du circuit et initialisation du temps
D7.write(1)# on place la broche d'alim du circuit à l'état haut  
t0 = time.time()*1e3# on initialise le temps (en ms)

# boucle d'acquisition des données
while ((flag==False) or (T[-1]-T[0])<=300) : 
    charge = 100*A0.read()# A0.read() entre 0 et 1
    temps = time.time()*1e3-t0
    T.append(temps)
    Q.append(charge)
    print(temps,";",charge)# on affiche
    flag = True

#################
# fin acquisition
#################
print("fin de l'acquisition")

########################
# on coupe le port série
########################
carte.exit()



"""

suite

du

programme

"""

