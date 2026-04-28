#Case1
a = int(input())
if a == 1:
    print('понедельник')
elif a == 2:
    print('вторник')
elif a == 3:
    print('среда')
elif a == 4:
    print('четверг')
elif a == 5:
    print('пятница')
elif a == 6:
    print('суббота')
elif a == 7:
    print('воскресенье')

#TheOne8
x = float(input())
y = float(input())
if (y >= 0) and (y <= 5) and (y <= (x**2 - 1)):
    print(True)
else:
    print(False)

#TheOne19
a = int(input())
l = int(input())
if a == 1:
    print(l*10)
elif a == 2:
    print(l*1000)
elif a == 3:
    print(l)
elif a == 4:
    print(l*0.001)
else:
    print(l*0.01)

#One41
a = int(input()) #123.456
a1 = a//100000
a2 = a//10000%10
a3 = a//1000%10
a4 = a//100%10
a5 = a//10%10
a6 = a%10
if (a1 == a6) and (a2 != a1) and (a2 != a3) and (a2 != a4) and (a2 != a5) and (a3 != a4) and (a4 != a5) and (a3 != a1) and(a4 != a1) and (a5 != a1):
    print(True)
else:
    print(False)

#Задача 5 №3
from math import sin
a = int(input())
b = int(input())
ygol = round(sin(int(input())/180 * 3.14),1)
print(0.5*a*b*ygol)

#Задача №6, пункт 8
print('Вычисление стоимости поездки на дачу')
print('Введите исходные данные:')
a = float(input('Расстояние от дачи в одну сторону (км) -> '))
b = float(input('Расход бензина (л на 100 км) -> '))/100
c = float(input('Цена литра бензина (руб.) -> '))
print('Поездка на дачу обойдется ', b*a*2*c, 'руб')