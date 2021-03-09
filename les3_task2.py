# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.

import random

# Создаем массив
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Ищем индексы четных чисел
even_num_idx = []
count = 0
for el in array:
    if el % 2 == 0:
        even_num_idx.append(count)
    count += 1
print(even_num_idx)