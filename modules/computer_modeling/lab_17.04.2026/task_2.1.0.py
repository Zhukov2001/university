from master_func import lagrannge_function

necessary_val = float(input("Введите число от 0.43 до 0.72: "))

data_x = [0.43,    0.48,    0.55,    0.62,    0.70,    0.75]
data_y = [1.63597, 1.73234, 1.87686, 2.03345, 2.28846, 2.35973]  

print(round(lagrannge_function(data_x, data_y, necessary_val), 5))