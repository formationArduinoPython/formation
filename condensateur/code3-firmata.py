from pyfirmata import Arduino, util
import time

carte = Arduino("/dev/ttyACM0", baudrate = 57600)
it = util.Iterator(carte)
it.start()

####################################
# ouverture d'un fichier en écriture
####################################
fichier = open("donnees.csv", "w")

########################
# définition des broches
########################
A0 = carte.get_pin("a:0:i")
D7 = carte.get_pin("d:7:o")

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

###########################
# première ligne du fichier
###########################
fichier.write("temps;charge")
fichier.write("\n")

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
    print(temps,";",charge)
    
    ##########################
    # écriture dans le fichier
    ##########################
    fichier.write(str(temps))
    fichier.write(";")
    fichier.write(str(charge))
    fichier.write("\n")
    ##########################

    flag = True



#################
# fin acquisition
#################
print("fin de l'acquisition")

###############################################
# on coupe le port série et on ferme le fichier
###############################################
carte.exit()
fichier.close()



#######################################################
# représentation des points expérimentaux sur un graphe
#######################################################
import matplotlib.pyplot as plt

plt.plot(T,Q, "b+", label = "points expérimentaux")


plt.xlabel("Temps en ms")
plt.ylabel("Charge en % du maximum")
plt.title("Charge d'un condensateur ; acquisition par PyFirmata")
plt.grid()

plt.show()


