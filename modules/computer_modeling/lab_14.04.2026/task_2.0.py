import math
import matplotlib.pyplot as plt
# Константы
mu = 0.029          
g = 9.8             
k = 1.38 * 10**-23       
T = 300            
p0 = 101325       
Na = 6.022e23      
# Масса одной молекулы воздуха
m = mu / Na         
# Концентрация у поверхности (из p0 = n0 * k * T)
n0 = p0 / (k * T)   
# Характерная высота
H = k * T / (m * g)   
# Функция для расчёта концентрации на высоте h
def concentration(n0, m, g, h, k, T):
    exponent = (-m * g * h) / (k * T)
    n = n0 * math.exp(exponent)
    return n
# Рисуем график зависимости n = n(h)
heights = []
concentrations = []
for h in range(0, 60000, 1000):   # от 0 до 60 км, шаг 1 км
    heights.append(h / 1000)      # переводим в км для графика
    concentrations.append(concentration(n0, m, g, h, k, T))
    
plt.plot(concentrations,heights,  color="blue", linewidth=2)
plt.grid(True)
plt.xlabel("Концентрация n")
plt.ylabel("Высота h, км")
plt.title("Зависимость концентрации молекул воздуха от высоты")
plt.show()

























