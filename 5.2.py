#Написать программу сложения и умножения двух 	шестнадцатеричных чисел. 
#При этом каждое число 	представляется как массив,
# элементы которого это цифры 	числа.


from collections import deque


def input_numbers():
    num = str(input('Введите шестнадцатиричное число: '))
    numbers = list(deque(num)) #т.к. по условию задачи хранить
                                #нужно в простом списке
    return list(numbers)


def read_numbers(numbers):
    values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    s = 0
    k = 0
    for i in range(len(numbers)):
        if numbers[i] in values:
            s = values[numbers[i]]
        else:
            s = int(numbers[i])
        k += s * 16 ** (len(numbers) - 1 - i)
    return k


def make_hexadecimal(num):
    num = int(num)
    values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque([])
    while num // 16 and num % 16 != 0:
       k = num % 16
       if k in values:
           result.appendleft(str(values[k]))
       else:
           result.appendleft(str(k))
       num = num // 16
    if num in values:
           result.appendleft(str(values[num]))
    elif num != 0:
           result.appendleft(str(num))
    return list(result)


def print_numbers(num):
    str_num = str()
    for i in num:
        str_num += i
    return str_num


print('Последовательно введите два шестнадцатиричных числа')
first_number = input_numbers()
second_number = input_numbers()
summ_numbers = make_hexadecimal(read_numbers(first_number) +
                                read_numbers(second_number))
multiplication_numbers = make_hexadecimal(read_numbers(first_number) *
                                          read_numbers(second_number))
#print(summ_numbers, multiplication_numbers)
print('Сумма введеных чисел в шестнадцатиричной системе: ',
      print_numbers(summ_numbers))
#print('Сумма введенных шестнадцатиричных чисел в десятичной системе: ',
#       read_numbers(summ_numbers)) 
print('Произведение введеных чисел в шестнадцатиричной системе: ',
      print_numbers(multiplication_numbers))

#print('Произведение введенных шестнадцатиричных чисел составит в десятичной системе: ', 
#      read_numbers( multiplication_numbers))
