x1 = int(input('Введите координату X для первой точки:'))
y1 = int(input('Введите координату Y для первой точки:'))
x2 = int(input('Введите координату X для второй точки:'))
y2 = int(input('Введите координату Y для второй точки:'))
dx = x2 - x1
dy = y2 - y1

print('Уравнение Вашей прямой:')
print('(y - ', y1, ') / ', dx, ' = (x - ', x1, ') / ', dy, sep='')