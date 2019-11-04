from pyfirmata import Arduino, util
import matplotlib.pyplot as plt
import numpy as np# pour la courbe théorique


# le baudrate est imposé à 57600, on ne peut pas prendre autre chose
carte = Arduino("/dev/ttyACM0", baudrate = 57600)
it = util.Iterator(carte)
it.start()

########################
# définition des broches
########################
# broche A0 ; on veut lire la valeur ana
A0 = carte.get_pin("a:0:i")#analog 0 input



#######################
# démarrage
#######################

print("START")
print("taper stop pour arrêter")

######################
# acquisition des différentes données et mesures
######################
v = 0.0   #intitialisation des variables
patm = 98.6 # pression atmosphérique
P,V = [],[]

while v != "stop" :
    try : 
        v=(input("Quel est le volume (en mL) ? : "))
        v=float(v)
        v = v*1e-6
        V.append(v)
        ana = A0.read()
        p = patm+(1/0.0018)*(ana-0.04)
        p=p*1000 # pour l'avoir en Pa
        P.append(p)
        print(v,"m3",";",p,"Pa")
    except :
        pass

"""
V = 1e-6*np.array([60,55,50,45,40,35,30,25])
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


########################
# courbe théorique GP
########################
V0 = 60e-6 # m^3
Vm = 24e-3 # m^3/mol
n = V0/Vm
R = 8.314
T = 18+273.15
a_modele_GP = n*R*T

print("a_modele_GP = ",a_modele_GP)

plt.plot(1/V, a_modele_GP/V, 'r-', label = "modèle du GP : p = nRT/V = {} $ \\times (1/V)$".format(round(a_modele_GP,2)))


########
# graphe
########
plt.grid()
plt.xlabel("1/V avec V en m^3")
plt.ylabel("pression en Pa")
plt.legend()
plt.show()


########################
# on coupe le port série
########################
carte.exit()


