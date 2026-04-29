# Задача 2 - Интервальный вариационный ряд
import matplotlib.pyplot as plt
import math

# Данные
data = [60, 25, 12, 10, 68, 35, 2, 17, 51, 9, 3, 130, 24, 85, 100, 152, 6, 18, 7, 42]
data_sorted = sorted(data)

# Количество интервалов по формуле Старджесса
n = len(data_sorted)
k = math.ceil(1 + 3.322 * math.log10(n))

# Величина интервала
min_val = min(data_sorted)
max_val = max(data_sorted)
width = math.ceil((max_val - min_val) / k)

# Создаем интервалы
intervals = []
frequencies = []

start = min_val
for i in range(k):
    end = start + width
    if i == k-1:
        count = sum(1 for x in data_sorted if start <= x <= end)
    else:
        count = sum(1 for x in data_sorted if start <= x < end)
    
    intervals.append((start, end))
    frequencies.append(count)
    start = end

# Выводим таблицу
print("Интервал (тыс.руб) | Частота")
print("-" * 35)
for i in range(len(intervals)):
    print(f"{intervals[i][0]:.0f} - {intervals[i][1]:.0f}{' ' * 10} | {frequencies[i]:^7}")

# Строим гистограмму
plt.figure(figsize=(10, 5))
plt.bar(range(len(frequencies)), frequencies, width=0.8, color='gray', edgecolor='black')
plt.xticks(range(len(intervals)), [f"{int(intervals[i][0])}-{int(intervals[i][1])}" for i in range(len(intervals))], rotation=45)
plt.grid(True, linestyle='--', alpha=0.7, axis='y')
plt.title('Интервальный вариационный ряд (гистограмма)', fontsize=14)
plt.xlabel('Размер вклада (тыс.руб)', fontsize=12)
plt.ylabel('Количество вкладов', fontsize=12)
plt.show()