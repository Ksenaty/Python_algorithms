# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


import random


def divided_sort(data):
    if len(data) > 2:
        size = len(data) // 2
        first = divided_sort(data[:size])
        second = divided_sort(data[size:])
        data = first + second

        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


SIZE = 10
array = [round(random.uniform(0, 49.99), 2) for i in range(SIZE)]
print(array)
print(divided_sort(array))
