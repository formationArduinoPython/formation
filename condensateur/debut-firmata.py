from pyfirmata import Arduino, util

# modifiez le nom du port (lisible en bas à droite sur l'IDE Arduino)
carte = Arduino("/dev/ttyACM0", baudrate = 57600)


it = util.Iterator(carte)
it.start()


"""

suite

du

programme

"""


carte.exit()


"""

suite

du

programme

"""

