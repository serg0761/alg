#В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.

import random

SIZE = 10
array = [random.randint(- SIZE * SIZE, SIZE * SIZE) for _ in range(SIZE)]

maximum = - SIZE * SIZE
for i in range(len(array)):
    if array[i] < 0:
        if array[i] > maximum:
            maximum = array[i]
            k = i
        else:
            pass
    else:
        pass
print('Массив:', array)
print('Максимальный отрицательны элемент в массиве:', maximum)
print('Его позиция в массиве:', k)
