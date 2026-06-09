def lagrannge_function(data_x, data_y, necessary_val):    
    result = 0
    for master in range(len(data_x)):
        # числитель
        numerator = 1
        # знаменатель
        denominator = 1
        # находим числитель
        for n in range(len(data_x)):
            if n != master:
                # находим числитель
                numerator *= necessary_val - data_x[n]
                # находим знаменатель 
                denominator *= data_x[master] - data_x[n]
        lagrange = numerator / denominator   
        result += lagrange * data_y[master]
    return result

def newton_function(data_x, data_y, necessary_val):
    n = len(data_x)
    h = round(data_x[1] - data_x[0], 10)

    # строим таблицу конечных разностей
    delta = [data_y.copy()]
    for order in range(1, 4):  # разности 1, 2, 3 порядка
        delta.append([])
        for j in range(len(delta[order - 1]) - 1):
            delta[order].append(round(delta[order - 1][j + 1] - delta[order - 1][j], 9))

    # интерполирование вперёд (x близко к началу таблицы)
    if necessary_val <= data_x[len(data_x) // 2]:
        # ищем подходящий узел x0
        x0 = data_x[0]
        index = 0
        for i in range(len(data_x) - 1):
            if data_x[i] <= necessary_val < data_x[i + 1]:
                x0 = data_x[i]
                index = i
                break

        q = (necessary_val - x0) / h

        # формула Ньютона вперёд
        result = (delta[0][index] +
                  q * delta[1][index] +
                  (q * (q - 1) / 2) * delta[2][index] +
                  (q * (q - 1) * (q - 2) / 6) * delta[3][index])

    # интерполирование назад (x близко к концу таблицы)
    else:
        # ищем подходящий узел xn
        xn = data_x[-1]
        index = len(data_x) - 1
        for i in range(len(data_x) - 1, 0, -1):
            if data_x[i - 1] < necessary_val <= data_x[i]:
                xn = data_x[i]
                index = i
                break

        q = (necessary_val - xn) / h

        # формула Ньютона назад
        result = (delta[0][index] +
                  q * delta[1][index - 1] +
                  (q * (q + 1) / 2) * delta[2][index - 2] +
                  (q * (q + 1) * (q + 2) / 6) * delta[3][index - 3])

    return result

    











