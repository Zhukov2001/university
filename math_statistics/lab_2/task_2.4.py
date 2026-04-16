import csv
import matplotlib.pyplot as plt
import math

dataset = []

# Сбор данных из CSV файла в "dataset"
with open('C:/Users/Danila/university-1/math_statistics/lab_2/developer_burnout_dataset_7000.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        dataset.append(row['commits_per_day'])

# Преобразование элементов dataset из тип "str" в "float"
for i in range(len(dataset)):
    if dataset[i] != "":
        dataset[i] = round(float(dataset[i]))

# Удаление пустых строк и сортировка dataset        
while "" in dataset:
    dataset.remove('')
else:
    dataset.sort()

# Создание вариантов из dataset путём превращения списка в множество
x_i = list(set(dataset))

# Величина интервала
k = math.ceil((1 + 1.4 * math.log(len(x_i))))
dk = math.ceil((max(x_i) - min(x_i)) / k)
# Создание списка где будут храниться частоты вариантов поиндексно
m_i = []
x_i1 = []
for i in range(0,len(x_i),dk):
    x_i1.append(x_i[i])
    tmp = 0
    for j in range(dk):
        tmp += dataset.count(x_i[i + j])
    m_i.append(tmp)

# Создание списка где будут храниться накопленные частоты
w_xi = [0]
for j in range(1, len(m_i)):
    tmp = 0
    for i in range(j):
        tmp += m_i[i]
    else:
        w_xi.append(tmp)

# 1) ======Среднее значение признака=======
arithmetic_mean = sum(x_i1) / len(x_i1)
print(f"1) Среднее значение признака - {arithmetic_mean}\n")

# 2) ========Дисперсия и среднее квадратическое отклонение=========
variance = 0

for count in x_i1:
    variance += (count - arithmetic_mean)**2
else:
    variance /= len(x_i1)
print(f"2.1) Дисперсия - {variance}\n")

mean_square = variance**0.5
print(f"2.2) Cреднее квадратическое отклонение - {mean_square}\n")

# 3) =========Мода======
mode = x_i[m_i.index(max(m_i))]

print(f"3) Мода - {mode}\n")

# 4) ======Медиана======
median = 0 
if len(x_i1) / 2 == 0:
    median = x_i1[len(x_i1) // 2]
else:
    median = (x_i1[len(x_i1) // 2] + x_i1[(len(x_i1) // 2) - 1]) / 2
print(f"4) Медиана - {median}\n")


# 5) ======Коэффициент вариации========
coefficient_variations = (mean_square / abs(arithmetic_mean)) * 100
coefficient_variations = round(coefficient_variations, 1)
print(f"5) Коэффициент вариации - {coefficient_variations}%\n")

# 6) ======Промежуток колебания плотности работников======

# print(f"6) Промежуток колебания плотности работников - ???\n")

# 7) ========Коэффициент ассиметрии=======

asymmetry_coefficient = 0

for count in x_i1:
    asymmetry_coefficient += (count + arithmetic_mean)**3
else:
    asymmetry_coefficient /= len(x_i1) * mean_square**3

print(f"7) Коэффициент ассиметрии - {asymmetry_coefficient}\n")


# 8) =======Эксцесс======

excess = 0
for count in x_i1:
    excess += (count + arithmetic_mean)**3
else:
    excess /= len(x_i1) * mean_square**4
    excess -= 3
print(f"8) Эксцесс - {excess}\n")


plt.subplot(1, 2, 1)
plt.plot(x_i1, m_i, color="black", marker='o', markersize=7)
plt.grid(which='major')
plt.title('Полигон')
plt.xlabel('Кол-во коммитов в день')
plt.ylabel('Количество программистов')

plt.subplot(1, 2, 2)
plt.plot(x_i1, w_xi, color="black", marker='o', markersize=7)
plt.grid(which='major')
plt.title('Кумулянта')
plt.xlabel('Кол-во коммитов в день')
plt.ylabel('Накопленные частоты')
plt.yticks(w_xi)

plt.show()


# print(*x_i1)
# print(*w_xi)
# print(*m_i)