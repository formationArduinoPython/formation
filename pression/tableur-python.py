import matplotlib.pyplot as plt
import numpy as np# pour la courbe théorique

#######################
# démarrage
#######################

print("START")
print("taper stop pour arrêter")

######################
# acquisition des difféentes données et mesure
######################
v = 0.0   #intitialisation des variables
P,V = [],[]

while v != "stop" :
    try : 
        v=(input("Quel est le volume (en mL) ? : "))
        v=float(v)
        p = float(input("Quel est la pression correspondante (en kPa) ? : "))
        v = v*1e-6
        V.append(v)
        p=p*1000 # pour l'avoir en Pa
        P.append(p)
        print(v,"m3",";",p,"Pa")
    except :
        pass

"""
V = [6.0e-05, 5.5e-05, 5.0e-05, 4.5e-05, 4.0e-05, 3.5e-05, 3.0e-05,
       2.5e-05]
P = 1000*np.array([101.4,110.1,120.5,132.3,148.5,169.3,198.8,238])
"""

#########################
# on exploite les données
#########################
P = np.array(P) ; V = np.array(V) # on transforme en tableaux numpy pour effectuer des opérations naturelles dessus

plt.plot(1/V, P, 'b+', label = "points expérimentaux") # on construit les pts expérimentaux



######################
# on cherche le modèle
######################
liste_coeffs = np.polyfit(1/V, P, 1) # fittage par polynôme de degré 1
a_modele_exp = liste_coeffs[0]
b_modele_exp = liste_coeffs[1]

# affichage des coeffs
print("a_modele_exp = ", a_modele_exp)
print("b_modele_exp = ", b_modele_exp)

# construction du modèle expérimental
plt.plot(1/V, a_modele_exp*(1/V)+b_modele_exp, 'g--',label = "modèle expérimental : p = {a} $ \\times (1/V) + $ {b}".format(a=round(a_modele_exp,2), b=round(b_modele_exp,0)))


########
# graphe
########
plt.xlim(0,40000)
plt.ylim(0,240000)
plt.grid()
plt.xlabel("1/V avec V en m^3")
plt.ylabel("pression en Pa")

plt.legend()
plt.show()
