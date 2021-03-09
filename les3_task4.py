# Определить, какое число в массиве встречается чаще всего.

import random

# Создаем массив
SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Считаем кол-во повторений каждого элемента
num = [i for i in range(MIN_ITEM, MAX_ITEM + 1)]
freq_num = []
for number in num:
    count = 0
    for el in array:
        if el == number:
            count += 1
    freq_num.append(count)

# Выводим количество повторений каждой цифры на экран
for i in range(len(num)):
    print(f'Цифра {num[i]} повторяется {freq_num[i]} раз')

# Ищем элемент, который повторяется максимальное кол-во раз
freq_max = freq_num[0]
freq_max_idx = 0
for i in range(len(freq_num)):
    if freq_num[i] > freq_max:
        freq_max = freq_num[i]
        freq_max_idx = i

# Выводим элемент, который повторяется максимальное кол-во раз, на экран
print('*' * 50)
print(f'Цифра {num[freq_max_idx]} повторяется наибольшее кол-во раз')
