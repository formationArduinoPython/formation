from matplotlib import pyplot as plt
import numpy as np

file = np.loadtxt("donnees2.csv", delimiter = ";", skiprows=1)
T = file[ : , 0]
Requiv = file[ : , 1]

plt.plot(T, Requiv, marker='+', label='mesures')
coeffs = np.polyfit(T, Requiv,1)
a, b = coeffs[0], coeffs[1]
Requiv_modele = a*T + b
plt.plot(T, Requiv_modele, '--r', label ='modèle')

print("Requiv_modele = {:.3f}*T + {:.3f}".format(a,b))
ecarttype=np.std(Requiv-Requiv_modele, ddof=1)
print('écart-type', ecarttype)

plt.title("thermistance")
plt.xlabel('température (°C)')
plt.ylabel('résistance équivalente (ohms)')
plt.legend()
plt.grid()
plt.show()
