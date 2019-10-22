# la courbe théorique est charge = charge_max*(1-exp(-temps/tau))
# soit en linéarisant : ln(1-charge/charge_max) = -temps/tau
Y = np.log(1-charge/charge_max)
coeffs = np.polyfit(temps, Y, 1)
a = coeffs[0]
b = coeffs[1]
tau = -1/a
print("tau = ", tau)
