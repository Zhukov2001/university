from master_func import newton_function

necessary_val = float(input("Введите число от 0.298 до 0.339: "))

data_x = [0.298, 0.303, 0.310, 0.317, 0.323, 0.330, 0.339]
data_y = [3.25578, 3.17639, 3.12180, 3.04819, 2.98755, 2.91950, 2.83598]

print(newton_function(data_x, data_y, necessary_val))