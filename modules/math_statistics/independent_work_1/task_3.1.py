# Задача 3 - Распределение по заработной плате
import matplotlib.pyplot as plt
import numpy as np

# Данные
intervals = ["До 5000", "5000-7000", "7000-10000", "10000-15000"]
frequencies = [5, 12, 7, 6]

# Для кумуляты нужны накопленные частоты
cumulative = []
total = 0
for freq in frequencies:
    total += freq
    cumulative.append(total)

# Выводим таблицу
print("Заработная плата (руб) | Частота | Накопленная частота")
print("-" * 55)
for i in range(len(intervals)):
    print(f"{intervals[i]:<20} | {frequencies[i]:^7} | {cumulative[i]:^19}")

# Рисуем два графика рядом
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Гистограмма
ax1.bar(intervals, frequencies, width=0.6, color='gray', edgecolor='black')
ax1.grid(True, linestyle='--', alpha=0.7, axis='y')
ax1.set_title('Гистограмма распределения', fontsize=12)
ax1.set_xlabel('Заработная плата (руб)', fontsize=10)
ax1.set_ylabel('Численность работников (чел)', fontsize=10)
ax1.tick_params(axis='x', rotation=45)

# Кумулята
x_pos = range(len(intervals))
ax2.plot(x_pos, cumulative, marker='o', color='black', linewidth=2, markersize=8)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_title('Кумулята (накопленные частоты)', fontsize=12)
ax2.set_xlabel('Заработная плата (руб)', fontsize=10)
ax2.set_ylabel('Накопленная частота', fontsize=10)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(intervals, rotation=45)

plt.tight_layout()
plt.show()