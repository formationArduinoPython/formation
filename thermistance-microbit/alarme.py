from microbit import *

Ualim = 3.13
R0 = 1000
Rlim = 123
intervalle = 10000

while True:
    """
    acquisition de Requivalente
    """
    valeurAnaUequiv = pin2.read_analog()
    Uequiv = valeurAnaUequiv*Ualim/1023
    Requiv = R0*Uequiv/(Ualim-Uequiv)
    print(Requiv)

    """
    réglage alarmes
    """
    if Requiv > Rlim:
        pin0.write_digital(0)
        pin1.write_digital(1)
    else:
        pin0.write_digital(1)
        pin1.write_digital(0)
    sleep(intervalle)





