#Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы.
#Задачу можно решить без сортировки исходного массива. 
#Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.

import random
import collections
import copy


m = 5
SIZE = 2 * m + 1
array = [random.randrange(1, 100) for _ in range(SIZE)]


def get_median(array):
    median_index = (len(array) - 1) / 2 + 1
    new_array = collections.Counter(copy.deepcopy(array))
    summ_score = 0
    while summ_score < median_index:
        current_med = min(new_array)
        summ_score += new_array[current_med]
        del new_array[current_med]
    return (array, current_med)


print(f'В списке: {get_median(array)[0]}, медиана= {get_median(array)[1]}')
