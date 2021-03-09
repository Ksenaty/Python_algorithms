# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы


import random

# Создаем массив
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


# Ищем максимальный и минимальный элемент массива
max_el = array[0]
min_el = array[0]
max_idx = 0
min_idx = 0
for i in range(len(array)):
    if array[i] > max_el:
        max_el = array[i]
        max_idx = i
    elif array[i] < min_el:
        min_el = array[i]
        min_idx = i
print(f'Максимальный элемент {max_el} с индексом {max_idx}')
print(f'Минимальный элемент {min_el} с индексом {min_idx}')

# Меняем максимальный и минимальный элемент местами
print(array)
array[max_idx], array[min_idx] = array[min_idx], array[max_idx]
print(array)
