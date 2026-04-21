# Задача 4 - Диаметры валиков
import matplotlib.pyplot as plt
import math

# Данные
data = [14.51, 14.42, 14.56, 14.47, 14.46, 14.35, 14.48, 14.53, 14.21, 14.31,
        14.35, 14.68, 14.56, 14.28, 14.36, 14.21, 14.52, 14.23, 14.41, 14.46,
        14.69, 14.54, 14.36, 14.15, 14.37, 14.51, 14.25, 14.55, 14.51, 14.36,
        14.62, 14.55, 14.38, 14.33, 14.40, 14.52, 14.48, 14.51, 14.55, 14.39,
        14.54, 14.58, 14.48, 14.37, 14.38, 14.51, 14.36, 14.15, 14.24, 14.32]

data_sorted = sorted(data)

# Количество интервалов
n = len(data_sorted)
k = math.ceil(1 + 3.322 * math.log10(n))

# Величина интервала
min_val = min(data_sorted)
max_val = max(data_sorted)
width = (max_val - min_val) / k

# Округляем для удобства
width = round(width, 2)

# Создаем интервалы
intervals = []
frequencies = []

start = min_val
for i in range(k):
    end = round(start + width, 2)
    if i == k-1:
        count = sum(1 for x in data_sorted if start <= x <= end)
    else:
        count = sum(1 for x in data_sorted if start <= x < end)
    
    intervals.append((start, end))
    frequencies.append(count)
    start = end

# Выводим таблицу
print("Интервал (мм) | Частота")
print("-" * 35)
for i in range(len(intervals)):
    print(f"{intervals[i][0]:.2f} - {intervals[i][1]:.2f} | {frequencies[i]:^7}")

# Строим гистограмму
plt.figure(figsize=(12, 6))

# Гистограмма
plt.bar(range(len(frequencies)), frequencies, width=0.8, color='gray', edgecolor='black')
plt.xticks(range(len(intervals)), [f"{intervals[i][0]:.2f}-{intervals[i][1]:.2f}" for i in range(len(intervals))], rotation=45)
plt.grid(True, linestyle='--', alpha=0.7, axis='y')
plt.title('Интервальный вариационный ряд (диаметры валиков)', fontsize=14)
plt.xlabel('Диаметр (мм)', fontsize=12)
plt.ylabel('Частота', fontsize=12)

# Добавляем значения над столбцами
for i, v in enumerate(frequencies):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# Дополнительная статистика
print("\nСтатистика:")
print(f"Всего измерений: {n}")
print(f"Минимальный диаметр: {min_val:.2f} мм")
print(f"Максимальный диаметр: {max_val:.2f} мм")
print(f"Количество интервалов: {k}")
print(f"Ширина интервала: {width:.2f} мм")