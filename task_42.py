#Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования Решета Эратосфена;
#Использовать алгоритм решето Эратосфена
# P.s. текст задания вставлялся после профайлинга функций. Нумерация строк смещена



def my_simple_numbers(n): #Максимально бессмысленный и беспощадный вариант
    simple_numbers = [2]
    i = 2
    while len(simple_numbers) < n:
        i += 1
        k = 0
        for j in range(2, i):
            if i % j == 0:
                k += 1
        if k == 0:
            simple_numbers += [i]
        else:
            k = 0
    return simple_numbers[len(simple_numbers) - 1]

#"task_42.my_simple_numbers(10)"
#100 loops, best of 3: 130 usec per loop
    
#my_simple_numbers(20)
#100 loops, best of 3: 596 usec per loop
    
#task_42.my_simple_numbers(30)
#100 loops, best of 3: 1.38 msec per loop


def clear_simple_numbers(n): #Банально брал верхнюю границу по известным простым числам.
    sieve = [i for i in range(n)]
    sieve[1] = 0
    
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    
    res = [i for i in sieve if i != 0]
    return res[len(res) - 1]

#task_42.clear_simple_numbers(30)
#100 loops, best of 3: 35.1 usec per loop
    
#task_42.clear_simple_numbers(72)
#100 loops, best of 3: 76.4 usec per loop

#"task_42.clear_simple_numbers(114)"
#100 loops, best of 3: 123 usec per loop
    

def full_eratosthenes(n): # Так и не понял, как определить верхнюю границу
                            #    диапазона натуральных чисел для поиска...
                            # Так что это сурово-экзотический вариант.
                            # И это точно Эратосфен, т.к. при необходимости массив
                            # с дырочками также можно вывести.
    simple_numbers = []
    k = 1
    while n > len(simple_numbers):
        sieve = [i for i in range(int(n*k))]
        sieve[1] = 0
        for i in range(2, int(n*k)):
            if sieve[i] != 0:
               j = i + i
               while j < int(n*k):
                   sieve[j] = 0
                   j += i
        
        simple_numbers = [i for i in sieve if i != 0]
        k += 1
    return simple_numbers[n - 1]
             
#task_42.full_eratosthenes(10)
#100 loops, best of 3: 122 usec per loop 
#"task_42.full_eratosthenes(20)"
#100 loops, best of 3: 413 usec per loop 
#"task_42.full_eratosthenes(30)"
#100 loops, best of 3: 672 usec per loop

           

#cProfile.run('my_simple_numbers(10)')  1    0.000    0.000    0.000    0.000 task_42.py:4(my_simple_numbers)
#cProfile.run('my_simple_numbers(20)')  1    0.001    0.001    0.001    0.001 task_42.py:4(my_simple_numbers)
#cProfile.run('my_simple_numbers(30)') 1    0.003    0.003    0.003    0.003 task_42.py:4(my_simple_numbers)

#cProfile.run('clear_simple_numbers(30)')        1    0.000    0.000    0.000    0.000 task_42.py:29(clear_simple_numbers)
#cProfile.run('clear_simple_numbers(72)')       1    0.000    0.000    0.000    0.000 task_42.py:29(clear_simple_numbers)
#cProfile.run('clear_simple_numbers(114)')        1    0.000    0.000    0.000    0.000 task_42.py:29(clear_simple_numbers)
    
#cProfile.run('full_eratosthenes(10)')    1    0.000    0.000    0.000    0.000 task_42.py:53(full_eratosthenes)
#cProfile.run('full_eratosthenes(20)')  1    0.000    0.000    0.000    0.000 task_42.py:53(full_eratosthenes)
#cProfile.run('full_eratosthenes(30)')         1    0.000    0.000    0.001    0.001 task_42.py:53(full_eratosthenes)
    
# =============================================================================
#Вывод:
# Не смотря на всю свою экзотичность full_eratosthenes побеждает my_simple_numbers
# Но лучше всего уметь определять верхнюю границу для поиска.
# Зависимость нелинейная, возможно, показательная.
# =============================================================================
