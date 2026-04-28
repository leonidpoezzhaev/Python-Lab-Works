#Задача 6 №2
from math import *
n = int(input())
x = float(input())
sym = x
for i in range(2,n+1):
    if i%2 == 0:
        sym -= (x**(i+1) / factorial(i+1))
    else:
        sym += (x**(i+2) / factorial(i+2))
print(sym)
print(sin(x))