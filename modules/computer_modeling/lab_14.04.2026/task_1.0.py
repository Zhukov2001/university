import math
import matplotlib.pyplot as plt

# Константы 
mu = 0.029      
g = 9.8         
R = 8.31        
T = 300         
p0 = 101325     

def main_function(p0, mu, g, h, R, T):
    var = ((-mu * g * h) / (R * T))
    var = p0 * math.exp(var)
    return var


# --- Задание 1.2: высота, где давление падает в e раз ---
height_2 = 0
while main_function(p0, mu, g, height_2, R, T) >= main_function(p0, mu, g, 0, R, T) / 2.7182:
    height_2 += 1 
print(f"Давление уменьшается на e на высоте: {(height_2 / 1000):.2f} км.")

# Задание 1.3
# Условимся: "практически ноль" = 0.1% от p0
height_3 = 0
while main_function(p0, mu, g, height_3, R, T) >= 0.1:
    height_3 += 1 
print(f"Давление практически равно нулю на высоте: {(height_3 / 1000):.2f} км.")

# Рисуем график

P = []
P_H = []

for height in range(0, 120000, 2000):
    P_H.append(main_function(p0, mu, g, height, R, T) / 1000)
    P.append(height / 1000)

plt.plot(P_H, P, color="black", markersize=10)
plt.grid(True)
plt.title('График зависимости P=P(h)')
plt.xlabel('Давление в кПа')
plt.ylabel('Высота в км')

plt.show()
