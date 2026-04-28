# Задача 6, пункт 2
def Mnozhiteli(x):
    vrem = x
    delitel = 2
    mnozhiteli = []
    while delitel != x:
        if vrem % delitel != 0:
            delitel += 1
        else:
            vrem //= delitel
            mnozhiteli.append(delitel)
    return mnozhiteli
print('Его простые множители:',*Mnozhiteli(int(input('Введите натуральное число: '))))