#Задача 3 пункт 4
from random import *
komp = randint(1,3)
igrok = int(input('Введите номер своего предмета, где 1 - это камень, 2 - это ножница, а 3 - бумага: '))
while komp == igrok:
    print("Один предмет! Загадываем снова)")
    komp = randint(1, 3)
    igrok = int(input('Введите номер своего предмета, где 1 - это камень, 2 - это ножница, а 3 - бумага: '))
if komp == 1 and igrok == 2:
    print('Компьютер выйграл!')
elif komp == 2 and igrok == 3:
    print('Компьютер выйграл!')
elif komp == 3 and igrok == 1:
    print('Компьютер выйграл!')
else:
    print('Поздравляю! Ты выйграл)')