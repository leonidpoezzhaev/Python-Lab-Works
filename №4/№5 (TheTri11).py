#TheTri11
def Symma(x):
    return sum([int(i) for i in str(x)])
def Palindrom(x):
    return str(x)==str(x)[::-1]
a = int(input('Введите начало промежутка: '))
b = int(input('Введите конец промежутка: '))
for i in range(a,b+1):
    if Palindrom((Symma(i))) == True:
        print(i, '- Палиндром!')
        flag = True
if not flag:
    print('No solution')