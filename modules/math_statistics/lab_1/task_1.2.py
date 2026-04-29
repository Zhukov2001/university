import numpy as np
import matplotlib.pyplot as plt
# Исходные данные 
data = [
    12, 6, 8, 6, 10, 11, 7, 10, 12, 8, 7, 7, 6, 7, 8, 6, 11, 9, 11,
    9, 10, 11, 9, 10, 7, 8, 8, 8, 11, 9, 8, 7, 5, 9, 7, 7, 14, 11,
    9, 8, 7, 4, 7, 5, 5, 10, 7, 7, 5, 8, 10, 10, 15, 10, 10, 13, 12,
    11, 15, 6
]
#Интервальный ряд
bins = np.arange(3.5, 16.5, 1)  # интервалы: (3.5,4.5], (4.5,5.5] и т.д.
freq, bin_edges = np.histogram(data, bins=bins)
# Середины интервалов
midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
# 2. Полигон частот
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(midpoints, freq, 'bo-', linewidth=2, markersize=8)
plt.title('Полигон')
plt.xlabel('Варианты')
plt.ylabel('Частота')
plt.grid(True, alpha=0.3)
for x, y in zip(midpoints, freq):
    plt.text(x, y + 0.3, str(y), ha='center', fontsize=9)
# 3. Кумулята (накопленные частоты)
cumulative_freq = np.cumsum(freq)
plt.subplot(1, 2, 2)
plt.plot(midpoints, cumulative_freq, 'rs-', linewidth=2, markersize=8)
plt.title('Кумулята')
plt.xlabel('Варианты')
plt.ylabel('Накопленная частота')
plt.grid(True, alpha=0.3)
for x, y in zip(midpoints, cumulative_freq):
    plt.text(x, y + 0.5, str(y), ha='center', fontsize=9)
plt.tight_layout()
plt.show()

