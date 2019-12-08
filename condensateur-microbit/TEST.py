import matplotlib.pyplot as plt
import numpy as np

# on sort les données, on les place dans 2 tableaux numpy
file = np.loadtxt("mb-donnees1.csv", skiprows=1, delimiter=';')
temps = file[ : ,0]
charge = file[ : ,1]


temps =  [209, 1845, 3639, 5459, 7340, 9298, 11187, 13161, 15068, 17293, 19260, 21166, 23149, 25116, 27031, 29014, 30981, 33396, 35380, 37346, 39261, 41245, 43220, 45135, 47118, 49093, 51008, 52992, 54967, 56882, 58866, 60780, 62695, 65662, 67637, 69552, 71536, 73519, 75434, 77418, 79393, 81307, 83283, 85258, 87173, 89156, 91131, 93055, 95039, 97014, 98929, 100912, 102939, 104940, 107010, 109071, 111072, 113160, 115221, 117222, 119292, 121353, 123354, 125381, 127443, 131359, 133437, 135438, 137595, 139742, 141838, 143925, 146013, 148100, 150187, 152274, 154379, 156509, 158596, 160701, 162849, 164944, 167109, 169257, 171353, 173474, 175614, 177758, 179906, 181996, 184101, 186248, 188344, 190449, 192605, 194700, 196796, 198936, 201031, 203196, 205344, 207440, 209605, 211752, 213857, 215987, 218083, 220205, 222335, 224431, 226527, 228623, 230719, 232875, 235022, 237118, 239283, 241431, 243527, 245692, 247839, 249935, 252074, 254170, 256275, 258422, 260518, 262614, 264710, 270419, 272515, 274620, 276767, 278863, 281028, 283184, 285280, 287445, 289602, 291758, 293907, 296001, 298097, 300245]
charge =  [19, 72, 125, 175, 223, 271, 314, 356, 394, 435, 470, 501, 532, 560, 586, 613, 636, 664, 684, 703, 721, 739, 756, 771, 783, 797, 809, 822, 833, 843, 853, 863, 871, 884, 891, 898, 905, 911, 918, 923, 928, 933, 938, 942, 946, 950, 954, 957, 961, 964, 967, 970, 973, 975, 978, 980, 982, 985, 987, 988, 989, 991, 993, 994, 995, 998, 999, 1000, 1001, 1002, 1007, 1007, 1004, 1005, 1006, 1007, 1007, 1008, 1009, 1009, 1010, 1010, 1011, 1011, 1012, 1013, 1013, 1013, 1014, 1014, 1014, 1015, 1015, 1015, 1016, 1016, 1016, 1016, 1016, 1017, 1016, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1018, 1018, 1018, 1018, 1018, 1019, 1019, 1019, 1021, 1023, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1020, 1019, 1020, 1020, 1020, 1020, 1020, 1020]


temps = np.array(temps)
charge = np.array(charge)

# ...
charge = charge*100/1023

# ...
plt.plot(temps, charge, 'b+', label = "points expérimentaux")

# variables pour étude théorique 
R = 270
C = 100e-6
tau = R*C
tau_us = tau*1e6
ChargeMax = 100

# ...
charge_theorie = ChargeMax*(1-np.exp(-temps/tau_us))

# ...
plt.plot(temps, charge_theorie, 'r--', label = "courbe théorique")


# axes, légendes,...
plt.legend()
plt.title("Charge d'un condensateur, R = {r}$\\Omega$, C = {c} F".format(r = R, c = C))
plt.xlabel("temps en us")
plt.ylabel("charge en %")
plt.grid()
plt.show()
