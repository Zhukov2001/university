from master_func import newton_function

necessary_val = float(input("Введите число от 1.215 до 1.260: "))

data_x = [ 1.215,    1.220,    1.225,    1.230,    1.235,    1.240,    1.245,    1.250,    1.255,    1.260]
data_y = [0.106044, 0.113276, 0.119671, 0.125324, 0.130328, 0.134776, 0.138759, 0.142367, 0.145688, 0.148809]

print(newton_function(data_x, data_y, necessary_val))
