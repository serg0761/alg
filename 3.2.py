import random

SIZE = 10   #Блок геренарции массива честно стибрил из разобранного на уроке
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
result = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        result += [i]
    else:
        pass
    
print('Старый массив:', array)

print('Его четные элементы:', result)
