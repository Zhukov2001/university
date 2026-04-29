# Задача 1 - Дискретный вариационный ряд
import matplotlib.pyplot as plt

# Данные
data = [4, 2, 4, 6, 5, 6, 4, 1, 3, 1, 2, 5, 2, 6, 3, 1, 2, 3, 4, 5, 4, 6, 2, 3, 4]

# Сортируем и находим уникальные значения
unique_values = sorted(set(data))

# Считаем частоты
frequencies = []
for value in unique_values:
    count = data.count(value)
    frequencies.append(count)

# Выводим таблицу
print("Тарифный разряд | Частота")
print("-" * 30)
for i in range(len(unique_values)):
    print(f"{unique_values[i]:^15} | {frequencies[i]:^7}")

# Рисуем полигон
plt.figure(figsize=(8, 5))
plt.plot(unique_values, frequencies, marker='o', color='black', linewidth=2, markersize=8)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Дискретный вариационный ряд', fontsize=14)
plt.xlabel('Тарифный разряд', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.xticks(unique_values)
plt.show()