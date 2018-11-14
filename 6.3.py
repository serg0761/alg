#В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы. 

import random
import sys


def show_size(x):
    summ_memory = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                summ_memory += show_size(key)
                summ_memory += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                summ_memory += show_size(item)
    return summ_memory


def happy_end(x):
    full_summ = 0
    for i in x:
        full_summ += show_size(i)
    return full_summ


def get_variables():
    loc_param = globals()
    unwanted = ['get_variables',  'show_size', 'happy_end', 'sys', 'random']
    param = []
    for k in loc_param:
        if '__' not in k:
            if k not in unwanted:
                param.append(loc_param[k])
    return param


SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
#Старый массив:  [2, 44, 79, 44, 75, 16, 97, 69, 59, 42]

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

print('Старый массив: ', array)
print('максимальный элемент:', maximum, 'минимальный элемент: ', minimum)
print('Новый массив:', new_array)
#Новый массив: [97, 44, 79, 44, 75, 16, 2, 69, 59, 42]
print(f'Итого было задействовано памяти: {happy_end(get_variables())}')
#Итого было задействовано памяти: 536
#print(get_variables())