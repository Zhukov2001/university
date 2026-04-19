import csv
import matplotlib.pyplot as plt

dataset = []

# Сбор данных из CSV файла в "dataset"
with open('C:/Users/Danila/university-1/math_statistics/developer_burnout_dataset_7000.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        dataset.append(row['daily_work_hours'])
        

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

# Создание списка где будут храниться частоты вариантов поиндексно
m_i = []
for opt in x_i:
    m_i.append(dataset.count(opt))

# Создание списка где будут храниться накопленные частоты
w_xi = [0]
for j in range(1, len(m_i)):
    tmp = 0
    for i in range(j):
        tmp += m_i[i]
    else:
        w_xi.append(tmp)

plt.subplot(1, 2, 1)
plt.plot(x_i, m_i, color="black", marker='o', markersize=7)
plt.grid(which='major')
plt.title('Полигон')
plt.xlabel('Время работы в день (часы)')
plt.ylabel('Количество программистов')
plt.xticks(x_i)

plt.subplot(1, 2, 2)
plt.plot(x_i, w_xi, color="black", marker='o', markersize=7)
plt.grid(which='major')
plt.title('Кумулянта')
plt.xlabel('Время работы в день (часы)')
plt.ylabel('Накопленные частоты')
plt.xticks(x_i)
plt.yticks(w_xi)
 
plt.show()











print(f"x_i {x_i}")
print(f"m_i {m_i}")
print(f"w_xi {w_xi}")

