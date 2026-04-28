'''Func41. Описать функцию Sin1(x, ε) вещественного типа (параметры x, ε — вещественные, ε > 0),
находящую приближенное значение функции sin(x):
sin(x) = x − x3/(3!) + x5/(5!) − … + (−1)n·x2·n+1/((2·n+1)!) + … .
В сумме учитывать все слагаемые, модуль которых больше ε. С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε.'''

from math import factorial, sin

def Sin1(x,e):
    if abs(x) <= e:
        return 0
    summ = x
    n = 0
    while True:
        n += 1
        element = (-1**n) * (x**(2*n+1)) / factorial(2*n+1)
        if abs(element) > e:
            summ += element
        else:
            break
    return summ
E = input('Введите 6 значений e через пробел (e>0): ').split()
X = float(input('Введите x: '))
for i in E:
    print(f'При e = {i}, синус равен {Sin1(X,float(i))}')
print(f'Точное значение синуса {sin(X)}')