def algorithm_1(set_A: list, set_B: list) -> int:
    """
    algorithm_1(set_A: list, set_B: list) -> int

    Функция возвращает суммарную стоймость перемещений
    из первого множества во второе

    Ключевые аргументы:
        set_A -- первое множество (из которого перемещаем элементы)
        set_B -- второе множество (в которое перемещаем элеенты)

    Допустимые значения аргументов: списки с целыми неотрицательными числами, без повторений

    Для удобного обращения к индексам использовал встроенную функцию .sort()
    """
    set_A.sort()
    set_B.sort()
    money_box = 0
    
    if len(set_A) % 2 == 0:

        while  len(set_A) != 2:
            # имитация перехода x_1 и x_2 в множество В    
            money_box += 2
            # имитация перехода x_1 обратно в множество А
            money_box += 1
            # переход x_n и x_(n-1) в множество B
            money_box += set_A[-1]
            set_B.extend([set_A.pop(-1), set_A.pop(-1)])
            # имитация перехода x_2 обратно в множество А
            money_box += 2

            set_B.sort()

        else:
            money_box += max(set_A)
            set_B.extend(set_A)
            set_A.clear()
    else:
        while  len(set_A) != 3:
            # имитация перехода x_1 и x_2 в множество В    
            money_box += 2
            # имитация перехода x_1 обратно в множество А
            money_box += 1
            # переход x_n и x_(n-1) в множество B
            money_box += set_A[-1]
            set_B.extend([set_A.pop(-1), set_A.pop(-1)])
            # имитация перехода x_2 обратно в множество А
            money_box += 2

            set_B.sort()

        else:
            set_A.sort()
            # имитация перехода x_1 и x_3 в множество B
            money_box += 3
            # имитация перехода x_1 обратно в множество A
            money_box += 1
            # имитация перехода x_1 и x_2 в множество В 
            money_box += 2

            # фактический переход всех оставшихся элементов в множество B
            set_B.extend(set_A)
            set_A.clear()


    set_B.sort()
    return money_box

def algorithm_2(set_A: list, set_B: list) -> int:
    """
    algorithm_2(set_A: list, set_B: list) -> int
    Функция возвращает суммарную стоймость перемещений
    из первого множества во второе

    Ключевые аргументы:
        set_A -- первое множество (из которого перемещаем элементы)
        set_B -- второе множество (в которое перемещаем элеенты)

    Допустимые значения аргументов: списки с целыми неотрицательными числами, без повторений

    Для удобного обращения к индексам использовал встроенную функцию .sort()
    """
    set_A.sort()
    set_B.sort()

    money_box = 0

    # имитация перемещения x_1 и x_2 из множества A  в множество B
    money_box += 2
    # имитация перемещения x_1 обратно в множество B
    money_box += 1
    # перемещение x_n и x_(n-1) из множества A  в множество B
    money_box += set_A[-1]
    set_B.extend([set_A.pop(-1), set_A.pop(-1)])
    # имитация перемещения x_2 обратно в множество B
    money_box += 2
    while len(set_A) != 2:
        # перемещение x_(n-k) и имитация перемещения x_1 из множества A 
        # в множество B. А так же имитация возвращени x_1 обратно в множество B
        money_box += set_A[-1] + 1
        set_B.append(set_A.pop(-1))
    else:
        # перемещения x_1 и x_2 из множества A  в множество B
        money_box += max(set_A)
        set_B.extend(set_A)
        set_A.clear()
    set_B.sort()
    return money_box
    
def algorithm_3(set_A: list, set_B: list) -> int:
    set_A.sort()
    set_B.sort()
    money_box = 0

data_base = [10, 100, 1_001, 10_000]

counter = 1
for test in data_base:
    data_A = [element for element in range(1, test + 1)]
    data_B = []

    print(F"Тест №{counter}")
    print(f"Объём первого множества: {test:_}")
    print(f"Цена первого алгоритма:{algorithm_1(data_A, data_B):_}")
    print(f"Цена второго алгоритма:{algorithm_2(data_B, data_A):_}")
    print()
    counter += 1