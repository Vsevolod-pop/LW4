from math import *
x = input('Введите x: ').replace(',', '.').strip()
while True:
    try:
        x = float(x)
        break
    except:
        x = input('Некорректное число. Пожалуйста, введите x корректно: ')
if x > 7.7:
    y = log10(x)*sin(3*x)
elif x == 7.7:
    y = ((x^5)-1)**(1/5)
else:
    y = 1+(cos(2*x))**3-3*(sin(3*x))**2
print('Искомый y =', y)
input('Нажмите ENTER для выхода')
