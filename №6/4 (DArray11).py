'''DArray11. В матрице размерности N x M найти значение первого
максимального элемента матрицы и его индексов.'''
n = int(input('Введите n (кол-во строк):'))
m = int(input('Введите m (кол-во столбцов): '))
matrixx = []
maxx = 0
for i in range(1,n+1):
    element = []
    for j in range(1,m+1):
        el = int(input(f'Введите элемент {i} строки, {j} столбца: '))
        element.append(el)
        if el > maxx:
            maxx = el
            index = [i,j]
    matrixx.append(element)

print('Ваша матрица:')
for i in matrixx:
    print(*i)
print(f'Максимальный элемент - {maxx}.\n'
      f'Он находится в {index[0]} строке и {index[1]} столбце.')