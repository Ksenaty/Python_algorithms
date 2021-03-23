# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.\

import random


def bubble_sort(data):
    n = 0
    while n <= len(data) - 1:
        counter = 0
        for i in range(len(data) - 1 - n):  # Улучшение: с каждой итерацией перестает проверять последние элементы
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                counter = 0
            else:
                counter += 1
        if counter == len(data) - 1 - n:  # Улучшение: функция закончится, как только список будет отсортирован
            break
        n += 1
    return array, n


SIZE = 20  # Размер массива
array = [random.randint(-100, 99) for i in range(SIZE)]
print(array)
print('*' * 100)
print(bubble_sort(array))
