import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]

minimum = maximum = array[0]

for i in range(1, len(array)):
    if array[i] > maximum:
        maximum = array[i]
        max_i = i
    elif array[i] < minimum:
        minimum = array[i]
        min_i = i
    else:
        pass
summa_between = 0

if min_i > max_i:
    for i in range(max_i + 1, min_i):
        summa_between += array[i]
else:
    for i in range(min_i + 1, max_i):
        summa_between += array[i]
print('Массив', array)
print('Максимальный элемент', maximum, 'имеет позицию', max_i)
print('Минимальный элемент', minimum, 'имеет позицию', min_i)
print('Сумма равна:', summa_between)
