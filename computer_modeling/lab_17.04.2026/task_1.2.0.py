necessary_val = float(input("Введите число от 1.215 до 1.260: "))

data_x = [ 1.215,    1.220,    1,225,    1.230,    1.235,    1.240,    1.245,    1.250,    1.255,    1.260]
data_y = [0.106044, 0.113276, 0.119671, 0.125324, 0.130328, 0.134776, 0.138759, 0.142367, 0.145688, 0.148809]

def newton_function(data_x, data_y, necessary_val):
    delta_y = [data_y.copy()]
    q = 0
    result = 0
    h = 0
    for order in range(1, 4):  # разности 1, 2, 3 порядка
        delta_y.append([])
        for j in range(len(delta_y[order - 1]) - 1):
            delta_y[order].append(round(delta_y[order - 1][j + 1] - delta_y[order - 1][j], 9))

    if necessary_val <= data_x[-3]:
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

            result = (delta_y[0][index] + 
              q * delta_y[1][index] + 
              (q * (q - 1) / 2) * delta_y[2][index] + 
              (q * (q - 1) * (q - 2) / 6) * delta_y[3][index])
 
    else:  
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
    return result

print(newton_function(data_x, data_y, necessary_val))
