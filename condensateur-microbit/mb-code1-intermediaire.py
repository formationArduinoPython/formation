from microbit import *

# on fixe t à 0 pour la suite
t = 0
# affichage ligne introduction du fichier
print("#t(ms);charge")

# décharge (au cas où) du condensateur pendant 300ms
# À COMPLÉTER
# À COMPLÉTER

###############################################
# boucle infinie pour tester l'état des boutons
###############################################
while True :
    # cas 1 : si on appuie sur le bouton A
    if button_a.is_pressed():
        # À COMPLÉTER : broche 8 à l'état haut
        # À COMPLÉTER : initialisation du temps t0 (en ms)
        # tant que t est plus petit que 300
        while (t <= 300):
            # À COMPLÉTER : mesure de t  
            # À COMPLÉTER : mesure de valeur analogique sur A0 (val) 
            # À COMPLÉTER : affichage de t;val

    # cas 2 : si on appuie sur le bouton B        
    if button_b.is_pressed():
        pin8.write_digital(0)
        sleep(1000)
        break # sortie de la boucle while
