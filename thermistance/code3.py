import matplotlib.pyplot as plt
import numpy as np

###########################
# définition des variables
###########################
T0 = 25
Ta = 30
Tb = 85
R0 = 1000
beta = 3730

R_L = 270

#########################
# abscisses : T en degrés
#########################
T = np.linspace(Ta,Tb,1000)
T_K = 273.15 + T
T0_K = 273.15 + T0

#####################################################
# expression de R_ctn et R_linearisee
#####################################################
R_ctn = R0*np.exp(beta*((1/T_K)-(1/T0_K)))

R_linearisee = R_L*R_ctn/(R_L+R_ctn)

#######################
# tracé de R_linearisee
#######################
plt.plot(T, R_linearisee, 'b-', label = "association de CTN et R_L = {} ohms en parallèle".format(R_L))

###########################################################
# modélisation de la caractéristique de l'association en //
###########################################################
liste_coeffs = np.polyfit(T, R_linearisee, 1)
a = liste_coeffs[0]
b = liste_coeffs[1]
print("a = ", a)
print("b = ", b)

########################################
# tracé du modèle de l'association en //
########################################
R_theorique_linearisee = a*T+b

plt.plot(T, R_theorique_linearisee, 'r--', label = "R_theorique_linearisee = {a}*T+{b}".format(a = round(a,2), b=round(b,0)))

#################################################
# différence manip / théorie pour modèle linéaire
#################################################
a_exp = -2.16
b_exp = 266
print("écart théorie vs expérience sur pente : ", round(((a_exp-a)/a)*100,1), " %")
print("écart théorie vs expérience sur ordonnée à l'origine : ", round(((b_exp-b)/b)*100,1), " %")

#######################
# axes, titre, légendes
#######################
plt.title("résistance équivalente CTN en // avec R_L")
plt.xlabel("Température en °C")
plt.ylabel("Valeur de la résistance R_ctn // R_L")
plt.legend()
plt.show()
