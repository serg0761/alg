import time

a = time.time()
print('Добрый день!')
name = str(input('Представьтесь, пожалуйста:'))
b = time.time()
c = int(((b - a) - int(b - a)) * 1000) / 1000

print(name, ', Ваше целое случайное число от 1 до 1000 = ',int(c*1000), sep='')

