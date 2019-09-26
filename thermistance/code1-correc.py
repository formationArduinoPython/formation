import matplotlib.pyplot as plt # ce paquet permettra de calculer et tracer la courbe
import numpy as np # cette bibliothèque permet de calculer facilement les images d'un tableau d'abscisses

###########################
# définition des variables
###########################
T0 = 25+273.15
Tb = 100+273.15
R0 = 1000
beta = 3730
###########################################################################
#on construit le tableau d'abscisses : entre Ta et Tb, on prend 1000 points
###########################################################################
T = np.linspace(T0,Tb,1000)

#####################################################
# on cherche l'image de ce tableau par la fonction R
#####################################################
Rtheorie = R0*np.exp(beta*((1/T)-(1/T0)))

#################################
# tracé et mise en page du graphe
#################################
plt.plot(T, Rtheorie, label = "caractéristique théorique")# on construit la courbe
plt.xlim(T0,Tb)
plt.xlabel("Températures en °K")#nom de l'axe des abscisses
plt.ylabel("Valeurs de la résistance de la CTN")#nom de l'axe des ordonnées
plt.title("Évolution théorique de la résistance de la CTN 1k en fonction de la température")
plt.grid()
plt.legend()
plt.show()

