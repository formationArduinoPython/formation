import serial

port_serie = serial.Serial("/dev/ttyACM0", 9600)

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
    file.write("\n")
    t=float(t);r=float(r)
    print(t,end='');print(';',end='');print(r)
    
file.close()

