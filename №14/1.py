'''File8. Даны имена двух файлов вещественных чисел. Известно, что первый из них существует и является непустым,
а второй в текущем каталоге отсутствует. Создать отсутствующий файл и записать в него начальный
и конечный элементы существующего файла (в указанном порядке).'''

import pickle

chisla = []
with open('input1.bin', 'rb') as f:
    while True:
        try:
            chisla.append(pickle.load(f))
        except Exception as e:
            break

print('Числа существующего файла:', *chisla)

with open('output1.bin', 'wb') as file:
    pickle.dump(chisla[0], file)
    pickle.dump(chisla[len(chisla)-1], file)

print('\nДанные из файла:')
with open('output1.bin', 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except Exception as e:
            break