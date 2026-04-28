#Func29
def AddRightDigit(D, K):
    if D < 0 or D > 9 or D % 1 != 0:
        D = int(input('Введите другое значение D: '))
        return AddRightDigit(D,K)
    elif K <= 0:
        K = int(input('Введите другое значение K: '))
        return AddRightDigit(D, K)
    else:
        return K*10+D
kk = int(input('Введите положительное число K: '))
for i in range(2):
    dd = int(input('Введите число D (в диапозоне от 0 до 9): '))
    kk = AddRightDigit(dd, kk)
    print('В результате получится:',kk)
