'''Spis13. Дан список целых чисел, содержащий как минимум два элемента.
Найдите в нём два ближайших элемента (то есть два элемента с
минимальной абсолютной разностью). Изменять список при этом нельзя.'''
spicok = list(map(int, input('Введите числа через пробел (min = 2): ').split()))
minn = max(spicok)
for i in range(1,len(spicok)):
    if abs(spicok[i-1]-spicok[i]) < minn:
        minn = abs(spicok[i-1]-spicok[i])
        elemnti = f'{spicok[i-1]}, {spicok[i]}'
print(elemnti)