import matplotlib.pyplot as plt
import numpy as np

file = np.loadtxt("donnees.csv", delimiter = ";", skiprows=1)
T = file[ : , 0]
Requiv = file[ : , 1]


plt.plot(T, Requiv, "b+", label = "points expérimentaux")

plt.xlabel("Températures °C")
plt.ylabel("Résistance Équivalente Rctn // RL")
plt.title("Valeurs de la Requiv en fonction de T")
plt.legend()
plt.show()
