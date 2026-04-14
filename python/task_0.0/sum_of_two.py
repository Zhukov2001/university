# Функция которая возвращает индексы чисел списка, которые в сумме дают желаемое значение
def sum_of_two(data, target):
    result = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                result.append([i, j])
    if len(result) == 0:
        return []
    elif len(result) == 1:
        return result[0]
    else:
        return result

# Функция которая запрашивает у пользователя и возвращает НАТУРАЛЬНОЕ число 
def enter_number():
    number = input("Enter your number: ")
    while not number.isdigit():
        number = input("Error! Only digit!\nEnter your number:  ")
    return int(number)

# Функция которая создаёт список с заданым размером состоящий из НАТУРАЛЬНЫХ числел
def list_of_number_creater(list_size):
    result_list = []
    for i in range(list_size):
        result_list.append(enter_number())
    return result_list

print("Please enter size list: ")
size = enter_number()

print("Enter the list items throught \"ENTER\": ")
data = list_of_number_creater(size)

print("Enter target: ")
target = enter_number()

result = sum_of_two(data, target)
print(f"Your result: {result}")
