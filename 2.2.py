# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).


import time


print('Расслабьтесь...')
time.sleep(1)
print('Сосредоточьтесь...')
time.sleep(1)
a = int(input('Запишите самое важное для Вас натуральное число...: '))
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
