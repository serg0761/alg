import random

SIZE = 10
array = [random.randint(-100, SIZE * SIZE) for _ in range(SIZE)]

maximum = - 10000
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