'''DArray8. Задана матрица A размерности n x n. Зеркально отразить ее
относительно главной диагонали'''
n = int(input('Введите размер матрицы: '))
matrixx = []
for i in range(1,n+1):
    element = []
    for j in range(1, n+1):
        element.append(int(input(f'Введите элемент {i} строки, {j} столбца: ')))
    matrixx.append(element)
print('Введенная матрица:')
for i in matrixx:
    print(*i)

print('-----')
print('Отзеркаленная матрица:')

for i in range(n):
    for j in range(i, len(matrixx)):
        matrixx[j][i], matrixx[i][j] = matrixx[i][j], matrixx[j][i]
for i in matrixx:
    print(*i)