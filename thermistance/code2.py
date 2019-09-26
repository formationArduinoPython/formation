import matplotlib.pyplot as plt
import numpy as np

###########################
# définition des variables
###########################
T0 = 25+273.15
Ta = 30+273.15
Tb = 80+273.15
R0 = 1000
beta = 3730

###########################################################################
T = np.linspace(Ta,Tb,1000)

#####################################################
# expression de R_ctn, R_L et R_linearisee
#####################################################
R_ctn = R0*np.exp(beta*((1/T)-(1/T0)))


for R_L in range(50, 650, 50) : 
    R_linearisee = R_L*R_ctn/(R_L+R_ctn)
    plt.plot(T, R_linearisee, label = "R_L = {} ohms".format(R_L))


plt.title("évolution de la caractéristique R_ctn en parallèle avec R_L") 
plt.xlabel("Température en °K")
plt.ylabel("Valeur de la résistance R_ctn // R_L")
plt.legend()
plt.show()
