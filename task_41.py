#Проанализировать скорость и сложность одного любого алгоритма, разработанных
# в рамках домашнего задания первых трех уроков.
# P.s. текст задания вставлялся после профайлинга функций. Нумерация строк смещена


#В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы. 

import cProfile
import random


def my_function(size):
    SIZE = size
    array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
    minimum = maximum = array[0]
    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]
        elif array[i] < minimum:
            minimum = array[i]
        else:
            pass
    new_array = []
    for i in range(len(array)):
        if array[i] == maximum:
            new_array += [minimum]
        elif array[i] == minimum:
            new_array += [maximum]
        else:
            new_array += [array[i]]
    return new_array

#task_41.my_function(10)
#100 loops, best of 3: 92 usec per loop
    
#task_41.my_function(100)
#100 loops, best of 3: 832 usec per loop
    
#task_41.my_function(1000)
#100 loops, best of 3: 8.92 msec per loop


def alex_function(size):
    SIZE = size
    array = [random.randint(-100, 100) for _ in range(SIZE)] 
    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i
    spam = array[idx_min]
    array[idx_min] = array[idx_max]
    array[idx_max] = spam
    return array

#task_41.alex_function(10)
#100 loops, best of 3: 80.2 usec per loop
    
#task_41.alex_function(100)
#100 loops, best of 3: 713 usec per loop

#task_41.alex_function(1000)
#100 loops, best of 3: 7.13 msec per loop
    


#cProfile.run('my_function(10)')     1    0.000    0.000    0.001    0.001 task_41.py:7(my_function)
#cProfile.run('my_function(100)')     1    0.000    0.000    0.004    0.004 task_41.py:7(my_function)
#cProfile.run('my_function(1000)')     1    0.002    0.002    0.013    0.013 task_41.py:7(my_function)

#cProfile.run('alex_function(10)')  1    0.000    0.000    0.000    0.000 task_41.py:38(alex_function)
#cProfile.run('alex_function(100)')   1    0.000    0.000    0.001    0.001 task_41.py:38(alex_function)
#cProfile.run('alex_function(1000)')         1    0.001    0.001    0.010    0.010 task_41.py:38(alex_function)
    
# =============================================================================
# Вывод: alex_function - WIN! Сложность практически линейная.
# =============================================================================
