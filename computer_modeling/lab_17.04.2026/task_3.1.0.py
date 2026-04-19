necessary_val = float(input("Введите число от 1.215 до 1.260: "))

data_x = [0.298, 0.303, 0.310, 0.317, 0.323, 0.330, 0.339]
data_y = [3.25578, 3.17639, 3.12180, 3.04819, 2.98755, 2.91950, 2.83598]

# Вычисление конечных разностей
delta_y = [data_y.copy()]  # delta_y[0] - исходные значения

for order in range(1, 4):  # разности 1, 2, 3 порядка
    delta_y.append([])
    for j in range(len(delta_y[order - 1]) - 1):
        delta_y[order].append(round(delta_y[order - 1][j + 1] - delta_y[order - 1][j], 9))

h = 0.005  # шаг

# Выбор формулы: вперед или назад
if necessary_val <= 1.245:  # интерполяция вперед
    # Находим x0 (начальный узел)
    for i in range(len(data_x) - 1):
        if data_x[i] <= necessary_val < data_x[i + 1]:
            h = round(data_x[i] - data_x[i - 1], 10)
            x0 = data_x[i]
            index = i
            break
    else:
        x0 = data_x[0]
        index = 0
    
    q = (necessary_val - x0) / h
    
    # Формула Ньютона вперед
    result = (delta_y[0][index] + 
              q * delta_y[1][index] + 
              (q * (q - 1) / 2) * delta_y[2][index] + 
              (q * (q - 1) * (q - 2) / 6) * delta_y[3][index])
    
    print(f"x0 = {x0}, q = {q}")
    
else:  # интерполяция назад
    # Находим xn (конечный узел)
    for i in range(len(data_x) - 1, 0, -1):
        if data_x[i - 1] < necessary_val <= data_x[i]:
            h = round(data_x[i] - data_x[i - 1], 10)
            xn = data_x[i]
            index = i
            break
    else:
        xn = data_x[-1]
        index = len(data_x) - 1
    
    q = (necessary_val - xn) / h
    
    # Формула Ньютона назад
    result = (delta_y[0][index] + 
              q * delta_y[1][index - 1] + 
              (q * (q + 1) / 2) * delta_y[2][index - 2] + 
              (q * (q + 1) * (q + 2) / 6) * delta_y[3][index - 3])
    
    print(f"xn = {xn}, q = {q}")

print(f"y({necessary_val}) ≈ {round(result, 6)}")