#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random
import copy

SIZE = 12
array = [random.random() * 50 for _ in range(SIZE)]


def merge_step(left, right):
    new_array = []
    while left and right:
        if left[0] > right[0]:
            new_array.append(left.pop(0))
        else:
            new_array.append(right.pop(0))
    if left:
        new_array.extend(left)
    if right:
        new_array.extend(right)
    return new_array


def mergesort(array):
    arr = copy.deepcopy(array)
    length = len(arr)
    if length >= 2:
        mid = int(length / 2)
        arr = merge_step(mergesort(arr[:mid]), mergesort(arr[mid:]))
    return arr


print(f'Исходный массив {array}')
print()
print(f'был отсортирован методом слияния: {mergesort(array)}')
