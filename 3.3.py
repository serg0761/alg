#В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы. 

import random

SIZE = 10
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
print('Старый массив: ', array)
print('максимальный элемент:', maximum, 'минимальный элемент: ', minimum)
print('Новый массив:', new_array)
