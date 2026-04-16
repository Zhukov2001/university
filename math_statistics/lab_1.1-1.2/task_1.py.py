import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
# 1. Исходные данные
data = [4, 0, 3, 4, 1, 0, 3, 1, 0, 4, 0, 0, 3, 1, 0, 1, 1, 3, 2, 3, 1, 2, 1, 2]
n = len(data)
# 2. Дискретный вариационный ряд
counter = Counter(data)
xi = sorted(counter.keys())          # варианты (баллы)
mi = [counter[x] for x in xi]        # частоты
# Накопленные частоты (кумулянта)
cum_mi = np.cumsum(mi).tolist()
# Частости (относительные частоты)
wi = [f / n for f in mi]
# Накопленные частости
cum_wi = [cm / n for cm in cum_mi]
#Графики: полигон и кумулянта
plt.figure(figsize=(14, 5))
#Полигон частот
plt.subplot(1, 2, 1)
plt.plot(xi, mi, marker='o', markersize=8,
         markerfacecolor='red', markeredgecolor='black',
         linestyle='-', linewidth=2, color='blue')
plt.xlabel("Варианты", fontsize=12)
plt.ylabel("m (частота)", fontsize=12)
plt.title("Полигон распределения результатов тестирования", fontsize=12, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.4)
plt.xticks(xi)
plt.xlim(min(xi) - 0.5, max(xi) + 0.5)
plt.ylim(0, max(mi) + 2)
#Подписи значений над точками
for x, m in zip(xi, mi):
    plt.text(x, m + 0.3, str(m), ha='center', va='bottom', fontsize=10, fontweight='bold')
#Кумулянта (полигон накопленных частот)
plt.subplot(1, 2, 2)
plt.plot(xi, cum_mi, marker='s', markersize=8,
         markerfacecolor='green', markeredgecolor='black',
         linestyle='-', linewidth=2, color='darkgreen')
plt.xlabel("Варианты", fontsize=12)
plt.ylabel("mₓ (накопленная частота)", fontsize=12)
plt.title("Кумулянта распределения результатов тестирования", fontsize=12, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.4)
plt.xticks(xi)
plt.xlim(min(xi) - 0.5, max(xi) + 0.5)
plt.ylim(0, max(cum_mi) + 2)
# Подписи значений над точками
for x, cm in zip(xi, cum_mi):
    plt.text(x, cm + 0.5, str(cm), ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.show()
