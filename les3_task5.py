# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random

# Создаем массив
SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Ищем максимальный элемент из отрицательных чисел
max_el = None
max_idx = None
for idx in range(len(array)):
    if array[idx] < 0:
        if max_el == None:
            max_el = array[idx]
            max_idx = idx
        if array[idx] > max_el:
            max_el = array[idx]
            max_idx = idx

# Выводим максимальный элемент из отрицательных чисел
print(f'Максимальный элемент из отрицательных чисел {max_el} с индексом {max_idx}')
