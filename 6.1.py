import sys


n = int(input('Введите целое трехзначное число '))
#'n = 152'
# ОС Windows 10, 32 бит

a = n - n // 10 * 10
b = n // 10 - n // 100 * 10
c = n // 100

result_mult = a * b * c
result_summ = a + b + c

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
    unwanted = ['get_variables',  'show_size', 'happy_end', 'sys']
    param = []
    for k in loc_param:
        if '__' not in k:
            if k not in unwanted:
                param.append(loc_param[k])
    return param


print(f'Произведение чисел Вашего целого трехзначного числа равно={result_mult}')
print(f'Сумма чисел Вашего целого трехзначного числа равна: {result_summ}')

print(f'Всего задействовано памяти: {happy_end(get_variables())}')
#Всего задействовано памяти: 84
#print(get_variables())
