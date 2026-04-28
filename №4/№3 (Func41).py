#Func41
from math import *
def Sin1(x, e):
    if e <= 0:
        e = float(input('Введите другое значение e'))
        return Sin1(x,e)
    else:
        if abs(x) > e:
            summ = x
        else:
            summ = 0
        chisla = 0
        schetchik = 0
        chetschet = 2
        while chisla != 6:
            vrem = (x**(3+schetchik))/factorial(3+schetchik)
            if abs(vrem) > e:
                if chetschet % 2 == 0:
                    summ -= vrem
                else:
                    summ += vrem
                chisla += 1
            schetchik += 2
            chetschet += 1
    return summ
print('Синус равен: ', Sin1(float(input('Введите X: ')), float(input('Введите e: '))))
print(sin(float(input())))