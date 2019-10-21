import serial

# pensez à entrer le nom de votre port série ci-dessous
# ce nom peut se trouver en bas à droite de l'IDE Arduino
port_serie = serial.Serial(port="nom_du_port_serie", baudrate=9600)



file = open("donnees2.csv", "w")
file.write("température;Réquivalente")
file.write("\n")

t = 100

while t > 30 :
    data = port_serie.readline()
    data = data.decode('ascii')
    data = data.split(";")
    t = data[0]
    r = data[1]
    file.write(t)
    file.write(";")
    file.write(r)
    # déjà un retour à la ligne dans le serial.println
    #file.write("\n") # donc cette ligne inutile
    t=float(t);r=float(r)
    print(t,end='');print(';',end='');print(r)
    
file.close()

