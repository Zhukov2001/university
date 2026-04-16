dataset = [4, 0, 3, 4, 1, 0, 3, 1, 0, 4, 0, 0, 3, 1, 0, 1, 1, 3, 2, 3, 1, 2, 1, 2]

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

# 1) ======Среднее значение признака=======
arithmetic_mean = sum(x_i) / len(x_i)
print(f"1) Среднее значение признака - {arithmetic_mean}\n")

# 2) ========Дисперсия и среднее квадратическое отклонение=========
variance = 0
for count in x_i:
    variance += (count - arithmetic_mean)**2
else:
    variance /= len(x_i)
print(f"2.1) Дисперсия - {variance}\n")
mean_square = variance**0.5
print(f"2.2) Cреднее квадратическое отклонение - {mean_square}\n")

# 3) =========Мода======
mode = x_i[m_i.index(max(m_i))]
print(f"3) Мода - {mode}\n")

# 4) ======Медиана======
median = 0 
if len(x_i) / 2 != 0:
    median = x_i[len(x_i) // 2]
else:
    median = (x_i[len(x_i) / 2] + x_i[(len(x_i) / 2) - 1]) / 2
print(f"4) Медиана - {median}\n")

# 5) ======Коэффициент вариации========
coefficient_variations = (mean_square / abs(arithmetic_mean)) * 100
coefficient_variations = round(coefficient_variations, 1)
print(f"5) Коэффициент вариации - {coefficient_variations}%\n")

# 7) ========Коэффициент ассиметрии=======
asymmetry_coefficient = 0
for count in x_i:
    asymmetry_coefficient += (count + arithmetic_mean)**3
else:
    asymmetry_coefficient /= len(x_i) * mean_square**3

print(f"7) Коэффициент ассиметрии - {asymmetry_coefficient}\n")

# 8) =======Эксцесс======
excess = 0
for count in x_i:
    excess += (count + arithmetic_mean)**3
else:
    excess /= len(x_i) * mean_square**4
    excess -= 3
print(f"8) Эксцесс - {excess}\n")





















# plt.subplot(1, 2, 1)
# plt.plot(x_i, m_i, color="black", marker='o', markersize=7)
# plt.grid(which='major')
# plt.title('Полигон')
# plt.xlabel('Набранные балы')
# plt.ylabel('Кол-во людей')


# plt.subplot(1, 2, 2)
# plt.plot(x_i, w_xi, color="black", marker='o', markersize=7)
# plt.grid(which='major')
# plt.title('Кумулянта')
# plt.xlabel('Набранные балы')
# plt.ylabel('Накопленная частота (люди)')
# plt.xticks(x_i)
# plt.yticks(w_xi)
 
# plt.show()

