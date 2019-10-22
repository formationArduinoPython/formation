import matplotlib.pyplot as plt


# listes obtenues lors de l'acquisition à coller ici
temperature_liste =  [81.9296, 80.9735, 80.3362, 80.6549, 80.6549, 79.3802, 79.0615, 78.4242, 78.1055, 76.8308, 76.8308, 76.5122, 76.1935, 75.8748, 75.2375, 75.5561, 74.2814, 73.9628, 73.9628, 73.6441, 72.6881, 72.0508, 72.6881, 71.7321, 71.4134, 70.7761, 70.1387, 69.5014, 69.8201, 69.1827, 68.5454, 68.2267, 68.5454, 68.5454, 68.5454, 68.5454, 67.9081, 67.9081, 67.2707, 67.2707, 66.6334, 65.996, 65.996, 65.996, 65.6773, 65.6773, 65.6773, 65.04, 65.04, 64.7213, 64.4027, 64.084, 63.7653, 63.4467, 63.4467, 63.1279, 62.4906, 62.4906, 62.172, 61.5346, 61.216, 61.5346, 61.5346, 60.8973, 60.26, 60.5786, 60.5786, 60.5786, 59.9413, 59.9413, 59.6226, 59.6226, 59.3039, 58.6666, 58.6666, 58.9853, 58.6666, 58.0293, 58.3479, 58.0293, 57.7106, 58.0293, 57.7106, 57.7106, 57.0732, 56.4359, 56.1172, 56.7546, 56.7546, 56.1172, 56.1172, 55.7985, 55.4799, 55.4799, 54.8426, 54.8426, 54.5239, 54.5239, 54.5239, 54.2052, 54.2052, 53.8866, 53.5679, 53.8866, 53.5679, 53.2492, 53.2492, 53.2492, 53.5679, 53.2492, 53.2492, 52.6119, 52.2932, 52.2932, 52.2932, 52.2932, 51.9745, 51.9745, 51.9745, 51.3372, 51.3372, 51.3372, 51.0185, 50.6998, 50.6998, 50.6998, 51.0185, 51.0185, 51.0185, 50.6998, 50.6998, 50.3811, 50.6998, 50.0625, 50.0625, 49.7438, 49.7438, 49.7438, 49.4252, 49.4252, 49.1065, 49.1065, 49.4252, 49.1065, 48.7878, 48.4692, 48.1505, 47.8318, 48.1505, 48.1505, 47.5132, 47.8318, 47.8318, 47.8318, 47.5132, 47.5132, 47.5132, 47.5132, 47.5132, 47.5132, 47.1945, 47.1945, 46.8758, 47.1945, 46.8758, 46.5572, 46.8758, 46.5572, 46.5572, 46.2385, 46.2385, 45.6011, 45.6011, 45.6011, 45.6011, 45.6011, 45.9198, 45.9198, 45.6011, 45.2825, 45.6011, 44.9638, 44.9638, 44.9638, 44.6451, 44.6451, 44.6451, 44.6451, 44.3264, 44.3264, 44.3264, 44.3264, 44.3264, 44.0078, 43.6891, 44.0078, 43.6891, 43.6891, 43.3704, 43.3704, 43.3704, 43.3704, 43.6891, 43.6891, 43.6891, 43.3704, 43.3704, 43.0518, 42.7331, 43.0518, 42.7331, 42.7331, 42.4144, 42.7331, 42.7331, 42.7331, 42.4144, 42.4144, 42.0958, 42.0958, 41.7771, 41.4584, 41.4584, 41.4584, 41.4584, 41.4584, 41.4584, 41.7771, 41.4584, 41.4584, 41.4584, 41.1397, 41.1397, 41.1397, 41.1397, 41.1397, 41.1397, 41.1397, 41.1397, 40.8211, 40.8211, 40.5024, 40.5024, 40.5024, 40.5024, 40.5024, 40.1837, 40.1837, 39.8651, 40.1837, 40.1837, 40.1837, 39.5464, 39.5464, 39.5464, 39.5464, 39.2277, 39.2277, 39.2277, 39.2277, 39.2277, 39.2277, 39.2277, 38.909, 38.909, 38.909, 38.909, 38.909, 38.909, 38.909, 38.909, 38.909, 39.2277, 38.5904, 38.5904, 38.5904, 38.2717, 38.5904, 38.2717, 38.2717, 37.953, 37.953, 37.953, 37.953, 37.953, 37.953, 37.6344, 37.6344, 37.6344, 37.953, 37.953, 37.6344, 37.953, 37.6344, 37.3157, 37.3157, 37.3157, 37.3157, 37.3157, 36.997, 36.997, 37.3157, 36.997, 36.997, 36.997, 36.997, 36.997, 36.997, 36.6784, 36.6784, 36.6784, 36.6784, 36.6784, 36.6784, 36.3597, 36.3597, 36.3597, 36.3597, 36.3597, 36.3597, 36.041, 36.041, 36.041, 36.041, 37.6344, 37.3157, 36.6784, 36.6784, 36.3597, 36.041, 35.7224, 36.041, 35.7224, 36.041, 35.7224, 35.4037, 35.4037, 35.4037, 35.4037, 35.4037, 35.4037, 35.4037, 35.4037, 35.7224]
Requiv_liste =  [99.9999, 101.184, 102.371, 102.371, 103.56, 103.56, 104.752, 104.752, 105.946, 107.143, 108.342, 109.544, 109.544, 111.956, 111.956, 113.166, 113.166, 114.379, 114.379, 115.594, 116.812, 116.812, 118.033, 119.256, 120.482, 120.482, 122.942, 121.71, 121.71, 122.942, 124.176, 125.413, 125.413, 125.413, 126.652, 127.894, 127.894, 127.894, 129.139, 130.387, 131.637, 132.89, 131.637, 131.637, 131.637, 132.89, 134.146, 134.146, 134.146, 135.405, 135.405, 136.667, 136.667, 137.931, 137.931, 137.931, 140.468, 140.468, 140.468, 140.468, 141.741, 141.741, 141.741, 143.017, 144.295, 144.295, 144.295, 144.295, 145.577, 146.861, 146.861, 146.861, 146.861, 148.148, 148.148, 148.148, 149.438, 150.731, 150.731, 149.438, 149.438, 150.731, 150.731, 152.027, 152.027, 153.326, 153.326, 153.326, 153.326, 154.628, 154.628, 155.932, 155.932, 157.24, 157.24, 157.24, 157.24, 157.24, 157.24, 157.24, 157.24, 158.55, 158.55, 158.55, 159.864, 159.864, 161.18, 161.18, 161.18, 162.5, 162.5, 162.5, 162.5, 162.5, 163.823, 163.823, 165.148, 165.148, 165.148, 166.477, 166.477, 166.477, 165.148, 165.148, 166.477, 166.477, 166.477, 166.477, 167.808, 167.808, 167.808, 169.143, 169.143, 169.143, 169.143, 170.48, 170.48, 170.48, 170.48, 170.48, 171.821, 171.821, 171.821, 171.821, 171.821, 173.165, 173.165, 173.165, 173.165, 174.512, 175.862, 175.862, 174.512, 174.512, 174.512, 175.862, 175.862, 175.862, 175.862, 175.862, 175.862, 175.862, 177.215, 177.215, 177.215, 178.571, 178.571, 177.215, 178.571, 178.571, 178.571, 179.931, 179.931, 179.931, 178.571, 179.931, 179.931, 179.931, 179.931, 179.931, 181.293, 181.293, 181.293, 181.293, 182.659, 182.659, 182.659, 182.659, 182.659, 182.659, 182.659, 184.028, 182.659, 184.028, 184.028, 184.028, 184.028, 184.028, 185.4, 185.4, 185.4, 185.4, 185.4, 185.4, 185.4, 186.775, 186.775, 186.775, 186.775, 186.775, 188.153, 188.153, 188.153, 188.153, 188.153, 188.153, 188.153, 188.153, 188.153, 188.153, 188.153, 188.153, 189.535, 189.535, 189.535, 190.92, 190.92, 189.535, 189.535, 190.92, 190.92, 190.92, 190.92, 190.92, 190.92, 190.92, 190.92, 190.92, 192.308, 192.308, 192.308, 192.308, 193.699, 193.699, 193.699, 193.699, 193.699, 193.699, 193.699, 193.699, 193.699, 193.699, 195.093, 195.093, 195.093, 195.093, 195.093, 195.093, 195.093, 195.093, 196.491, 195.093, 195.093, 195.093, 196.491, 196.491, 196.491, 196.491, 196.491, 196.491, 196.491, 196.491, 196.491, 197.892, 197.892, 197.892, 197.892, 197.892, 197.892, 197.892, 197.892, 197.892, 197.892, 197.892, 197.892, 199.297, 199.297, 199.297, 199.297, 199.297, 199.297, 199.297, 199.297, 199.297, 199.297, 199.297, 199.297, 200.704, 200.704, 200.704, 200.704, 200.704, 200.704, 200.704, 200.704, 200.704, 200.704, 200.704, 200.704, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 202.115, 203.529, 203.529, 200.704, 202.115, 202.115, 202.115, 203.529, 203.529, 203.529, 203.529, 203.529, 203.529, 203.529, 203.529, 203.529, 203.529, 203.529, 204.947, 204.947, 204.947, 204.947, 204.947]


plt.plot(temperature_liste, Requiv_liste, "b+", label = "points expérimentaux")

plt.xlabel("Températures °C")
plt.ylabel("Résistance Équivalente Rctn // RL")
plt.title("Valeurs de la Requiv en fonction de T")
plt.legend()
plt.show()