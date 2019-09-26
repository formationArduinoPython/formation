import matplotlib.pyplot as plt
import numpy as np

#####################################################
# extraction des données sous forme de tableaux numpy
#####################################################
file = np.loadtxt("donnees.csv", delimiter = ";", skiprows=1)
T = file[ : , 0]
Requiv = file[ : , 1]

###############################
# recherche de la droite modèle
###############################
liste_coeffs = np.polyfit(T, Requiv, 1)
a = liste_coeffs[0]
b = liste_coeffs[1]
print("a = ", a)
print("b = ", b)
Requiv_modele = a*T+b # équation de la droite modèle

############################
# tracé points expérimentaux
############################
plt.plot(T, Requiv, "b+", label = "points expérimentaux")

#####################
# tracé courbe modèle
#####################
plt.plot(T, Requiv_modele, "r--", label = "modèle expérimental : Requiv = {a}*T+{b}".format(a = round(a,2), b = round(b,0)))

######################
# axes, titre, légende
######################
plt.xlabel("Températures °C")
plt.ylabel("Résistance Équivalente Rctn // RL")
plt.title("Valeurs de la Requiv en fonction de T")
plt.legend()
plt.show()
