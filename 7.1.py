#Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
#заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).


import random
import copy

SIZE = 10
array = [random.randrange(-100, 100) for _ in range(SIZE)]


def my_sort(array):
    new_arr = copy.deepcopy(array)
    n = 1
    k = False
    while n < len(new_arr) and k is not True:
        k = True
        for i in range(len(new_arr) - n):
            if new_arr[i] < new_arr[i+1]:
                new_arr[i], new_arr[i+1] = new_arr[i+1], new_arr[i]
                k = False
        n += 1
    return(array, new_arr)


print(f'Исходный список: {my_sort(array)[0]}')
print(f'Отсортированный список: {my_sort(array)[1]}')
