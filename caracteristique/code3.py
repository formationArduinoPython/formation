import numpy as np
import matplotlib.pyplot as plt

###########################################
# extraction des données dans deux tableaux
###########################################

file = np.loadtxt("data", skiprows = 1, delimiter =";")

ValeurAna_Ug = file[:,0]
ValeurAna_Ur = file[:,1]

####################################################################
# Transformation des valeurs analogiques en tensions correspondantes
####################################################################

Ug = # à compléter
Ur = # à compléter

################################
# Trouver les grandeurs Ud et Id
################################

# valeur de la résistance R du circuit
R = # à compléter

Ud = Ug-Ur# à justifier

Id = # à compléter


#############################
# tracé de la caractéristique
#############################

plt.plot(Id, Ud, label = "caractéristique expérimentale")
plt.ylabel("Tension $U_d$ aux bornes de la LED (en Volts)")
plt.xlabel("Intensité $I_d$ traversant la LED (en Ampères)")
plt.title("Caractéristique de la LED")
plt.grid()



"""
####################################
# modélisation de la première partie
####################################

Us = # à compléter

x1 = # à compléter
y1 = # à compléter
x2 = # à compléter
y2 = # à compléter

modele1_Id=[x1, x2]
modele1_Ud=[y1, y2]

plt.plot(modele1_Id, modele1_Ud, 'r--', label = "partie 1, modélisation")
"""



"""
####################################
# modélisation de la seconde partie
####################################

# On extrait les éléments i dans la portion linéaire
# On cherche leur référence dans Ud
# On cale tt ça dans des listes vierges

Ud2, Id2 = [], []
# on transforme Id et Ud en liste
Id = list(Id)
Ud = list(Ud)

x_min = # à compléter
x_max = # à compléter

for i in Id :
    if i >=x_min and i<=x_max : # dans l'intervalle où c'est droit
        indice = Id.index(i)
        u = Ud[indice]
        Ud2.append(u)
        Id2.append(i)

# on met ces listes en tableaux
Ud2 = np.array(Ud2)
Id2 = np.array(Id2)

# on modélise ce comportement

coeffs = np.polyfit(Id2, Ud2, 1)

K2 = coeffs[0]
K3 = coeffs[1]

modele2_Ud = K2*Id2 + K3
"""




"""
#########################################
# Représentation de la partie 2 du modèle
#########################################

plt.plot(Id2, modele2_Ud, 'r-.', label = "partie 2, modélisation")
"""



plt.legend()
plt.show()
















