# modelisation-experimentale-intermediaire.py

import matplotlib.pyplot as plt
import numpy as np

# IMPORTATION DES DONNÉES DU FICHIER DANS DEUX LISTES T et Requiv
file = np.loadtxt("donnees.csv", delimiter = ";", skiprows=1)
T = file[ : , 0]
Requiv = file[ : , 1]

# REPRÉSENTATION DES POINTS EXPÉRIMENTAUX SUR UN GRAPHE
plt.plot()# À COMPLÉTER

# AMÉLIORATIONS
plt.xlabel()# À COMPLÉTER
plt.ylabel()# À COMPLÉTER
plt.title()# À COMPLÉTER
plt.legend()
plt.show()
