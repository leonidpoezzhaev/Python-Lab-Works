#Задача 5 №3
from math import sin
a = int(input())
b = int(input())
ygol = round(sin(int(input())/180 * 3.14),1)
print(0.5*a*b*ygol)