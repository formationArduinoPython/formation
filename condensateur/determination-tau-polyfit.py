# la courbe théorique est charge = ChargeMax*(1-exp(-temps/tau))
# soit en linéarisant : ln(1-charge/ChargeMax) = -temps/tau
Y = np.log(1-charge/ChargeMax)
coeffs = np.polyfit(temps, Y, 1)
a = coeffs[0]
b = coeffs[1]
tau = -1/a
print("tau = ", tau)
