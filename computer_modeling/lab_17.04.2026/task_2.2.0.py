from master_func import lagrannge_function

necessary_val = float(input("Введите число от 0.43 до 0.72: "))

data_x = [1.375,    1.38,    1.385,    1.39,    1.395,    1.4]
data_y = [5.04192, 5.17744, 5.32016, 5.47069, 5.62968, 5.79788]  

print(round(lagrannge_function(data_x, data_y, necessary_val), 5))