# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).


import time
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
    unwanted = ['get_variables',  'show_size', 'happy_end', 'sys', 'time']
    param = []
    for k in loc_param:
        if '__' not in k:
            if k not in unwanted:
                param.append(loc_param[k])
    return param


print('Расслабьтесь...')
time.sleep(1)
print('Сосредоточьтесь...')
time.sleep(1)
z = a = int(input('Запишите самое важное для Вас натуральное число...: '))# 3578
# т.к. значение обнуляется = > объем памяти меняются во время выполнения скрипта для наглядности беру две переменные
# иначе ответ получается как и в предыдущей задаче, скука же. А обнуляющуюся переменную можно, при желании, исключить.

devil_even = 0
devil_uneven = 0


if a == 0:
    print('Ваш очень важный ноль сугубо четный')
else:
    while a != 0:
        c = a % 10 % 2
        a = a // 10
        if c == 0:
            devil_even += 1
        else:
            devil_uneven += 1
    print('Ваше самое важное число содержит:')
    print(devil_even, '- четных')
    print(devil_uneven, '- нечетных')



print('До новых встреч!')
print(f'Итого было задействовано памяти: {happy_end(get_variables())}')
#Итого было задействовано памяти: 68
#print(get_variables())
