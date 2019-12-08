import serial

# il faudra sans doute modifier le nom du port sur lequel est branchée la carte microbit
port_serie = serial.Serial(port = "/dev/ttyACM0", baudrate = 115200)

# ouverture d'un fichier en écriture pour sauvegarde des données
file = open("donnees.csv", "w")

# création de listes vides pour placer les données
temps, charge = [], []

# un booléen pour rentrer dans la boucle, temps max d'acquisition
fin = False
temps_acquisition = 300

# on rentre dans la boucle d'acquisition
while (fin == False or (temps[-1]-temps[0]) <= temps_acquisition):
    ligne_recue = port_serie.readline()#ligne reçue b'.....\r\n' donc en bytes
    ligne_recue_str = ligne_recue.decode("ascii")#on trsf en str
    ligne_recue_str_list = ligne_recue_str.split(";")#on crée une liste en spécifiant que le séparateur est ;
    try :
        print(ligne_recue_str_list)
        t = float(ligne_recue_str_list[0])#on pd 1ère valeur de liste qui est un string en le transformant en float
        q = float(ligne_recue_str_list[1])#on prend 2ème valeur de liste qui est un string en le transformant en float
        temps.append(t)
        charge.append(q)
        fin = True
        #on ecrit dans un fichier csv pour svgd la ligne transformée de bytes en string
        file.write(ligne_recue_str) 
    except :
        pass

file.close()
port_serie.close()


###########################################
# représentation des données expérimentales
###########################################
import matplotlib.pyplot as plt
import numpy as np
temps = np.array(temps)
charge = np.array(charge)
charge = 100*charge/1023

plt.plot(temps, charge, 'b+', label = "points expérimentaux")

##################
# modèle théorique
##################

# variables pour étude théorique 
R = 270
C = 100e-6
tau = R*C
tau_ms = tau*1e3
ChargeMax = 100

# calcul charge théorique
charge_theorie = ChargeMax*(1-np.exp(-temps/tau_ms))

# représentation charge théorique
plt.plot(temps, charge_theorie, 'r--', label = "courbe théorique")


# axes, légendes,...
plt.legend()
plt.title("Charge d'un condensateur, R = {r}$\\Omega$, C = {c} F".format(r = R, c = C))
plt.xlabel("temps en ms")
plt.ylabel("charge en %")
plt.grid()
plt.show()

