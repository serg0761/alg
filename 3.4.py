#Определить, какое число в массиве встречается чаще всего. 

import random

SIZE = 10
array = [int(random.expovariate(0.05)) for _ in range(SIZE)] 
# иначе постоянно уникальные числа получаются, а тут хоть какое-то повторение.
k = 1
#element = array[0]

for ar in array:    
    c = 0
    for i in array:
        if ar == i:
            c +=1
        else:
            pass
    if c > k:
        k = c
        element = ar
    else:
        pass
if k > 1:
    print('Массив: ', array)
    print('Наиболее часто в нем встречается число', element)
    print('Оно встречается', k, 'раз')
else:
    print('Массив: ', array)
    print('Предложенный массив серый и скучный, т.к. все элементы уникальные')

    