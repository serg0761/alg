#Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ»
# в каждой строке.

i = 32

while i < 128:
    print(str(i), '-' , chr(i), end=' ')
    if (i - 1) % 10 == 0:
        print()
    i += 1
