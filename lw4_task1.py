from math import *
x = input('Введите x: ').strip().replace(',','.')
while True:
    try:
        x = float(x)
        if -1 >= x or x >= 1:
            raise Exception
    except Exception:
        x = input('Некорректное число. Пожалуйста, введите x: ').strip().replace(',', '.')
    else:
        x = float(x)
        break
y = input('Введите y: ').strip().replace(',','.')
while True:
    try:
        y = float(y)
        if -1 >= y or y >= 1:
            raise Exception
    except Exception:
        y = input('Некорректное число. Пожалуйста, введите y: ').strip().replace(',', '.')
    else:
        y = float(y)
        break
z = log10((sin(x*x)/(fabs(cos(y))+2)))
print('Искомое значение z =', z)
print("GIT")







"""while True:
    try:
        if x[0] == '-':
            raise Exception
        if ',' in x:
            x = x.replace(',', '.')
        float(x)
    except Exception:
        x = input('Некорректное число. Пожалуйста, введите x: ')
    else:
        x = float(x)
        break
y = input('Введите y: ')
while True:
    try:
        if y[0] == '-':
            raise Exception
        if ',' in y:
            y = y.replace(',','.')
        float(y)
    except Exception:
        y = input('Некорректное число. Пожалуйста, введите y: ')
    else:
        y = float(y)
        break
z = input('Введите z: ')
while True:
    try:
        if z[0] == '-':
            raise Exception
        if ',' in z:
            z = z.replace(',','.')
        float(z)
    except Exception:
        z = input('Некорректное число. Пожалуйста, введите z: ')
    else:
        z = float(z)
        break
if (x < y+z) and (y < x+z) and (z < x + y):
    p = (x + y + z) / 2
    S = sqrt(p*(p-x)*(p-y)*(p-z))
    print('Площадь треугольника равна =', S)
else:
    print('Треугольника с заданными сторонами не существует ')
input('Нажмите ENTER для выхода')"""
