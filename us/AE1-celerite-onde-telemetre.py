import matplotlib.pyplot as plt
import numpy as np

#création des listes contenant les mesures réalisées
dM=[]
dS=[]
for i in range(10):
    dM.append(float(input("valeur en mètre de la distance dM mesurée à la règle")))
    dS.append(float(input("valeur en mètre de la distance dS mesurée avec le télémètre")))

# Tracé du graphique
plt.xlabel("dM (m)")
plt.ylabel("dS (m)")
plt.plot(dM,dS,"b+")


# modélisation des points expérimentaux par une droite dM = a dS + b
a=np.polyfit(dM,dS,1)[0] # pente de la droite
b=np.polyfit(dM,dS,1)[1] # ordonnée à l'origine
dM_modele = np.linspace(0,max(dM),100)
dS_modele = a*dM_modele+b
plt.plot(dM_modele,dS_modele,"r-",label="modélisation")
plt.annotate("l'équation de la droite modèle est " + str(round(a,3)) +" * dM + "+ str(round(b,3)), xy=(0, 0))
plt.legend()
plt.show()




