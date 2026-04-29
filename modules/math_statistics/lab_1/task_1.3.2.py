import csv
import matplotlib.pyplot as plt
import math

dataset = []

# Сбор данных из CSV файла в "dataset"
with open('C:/Users/Danila/university-1/math_statistics/developer_burnout_dataset_7000.csv', mode='r', newline='') as csv_file:
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