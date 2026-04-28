'''Spis22. Напишите программу, которая вычисляет арифметическое
выражение, введённое в виде символьной строки. Выражение содержит
только целые числа, знаки арифметических действий (сложения,
вычитания, умножения и деления) и круглые скобки правильной
вложенности.'''
def index_element(spicok):
    for i in range(len(spicok)-1,-1,-1):
        if spicok[i] == ')':
            return i

def open_brackets(massiv, left, right):
    new_massiv = massiv[left:right]
    if '(' in new_massiv:
        left = new_massiv.index('(')+1
        right = index_element(new_massiv)
        return new_massiv[:left-1] + [str(vicheslit(open_brackets(new_massiv, left, right)))]+ new_massiv[right+1:]
    else:
        return new_massiv

def vicheslit(massiv):
    while '*' in massiv:
        first = massiv.index('*')-1
        second = massiv.index('*')+1
        massiv = massiv[:first]+[str(int(massiv[first])*int(massiv[second]))]+massiv[second+1:]
    while '/' in massiv:
        first = massiv.index('/') - 1
        second = massiv.index('/') + 1
        massiv = massiv[:first] + [str(int(int(massiv[first]) / int(massiv[second])))] + massiv[second+1:]
    while len(massiv) != 1:
        if massiv[1] == '+':
            massiv = [str(int(massiv[0]) + int(massiv[2]))] + massiv[3:]
        else:
            massiv = [str(int(massiv[0]) - int(massiv[2]))] + massiv[3:]
    return massiv[0]

primer = [i for i in input('Введите пример: ')]
primer2 = []
i = 0
last = 0
element = ''
while i < len(primer):
    if primer[i] in '0123456789':
        if last == (i-1):
            primer2[last] += primer[i]
        else:
            primer2.append(primer[i])
        last = i
        i += 1
    else:
        if primer[i] in '+-*/':
            primer2.append(primer[i])
            i += 1
        else:
            left = i+1
            right = index_element(primer)
            primer2.append(vicheslit(open_brackets(primer,left,right)))
            i = right+2
print(f'Ответ: {vicheslit(primer2)}')




