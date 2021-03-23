# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


import random


def gnome_sort(data):    # был соблазн попробовать Bogosort :)
    i = 0
    j = 1
    while i < len(data) - 1:
        if data[i] < data[i + 1]:
            i = j
            j += 1
        else:
            data[i], data[i + 1] = data[i + 1], data[i]
            i -= 1
            if i == -1:
                i = j
                j += 1

    return array


m = 6
SIZE = 2 * m + 1
LEFT_BORDER = 0
RIGHT_BORDER = 99
array = [random.randint(LEFT_BORDER, RIGHT_BORDER) for i in range(SIZE)]
print(array)
gnome_sort(array)
print(array)
print('Медиана ', array[len(array) // 2])
print('Элементы меньше медианы: ', array[:len(array) // 2])
print('Элементы больше медианы: ', array[len(array) // 2 + 1:])
