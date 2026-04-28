'''File36. Дан файл целых чисел. Удвоить его размер, записав в конец
файла все его исходные элементы (в том же порядке).'''

import pickle

chisla = []
with open('input3.bin', 'rb') as f:
    while True:
        try:
            chisla.append(pickle.load(f))
        except Exception as e:
            break

print('Исходные элементы:', *chisla)
print('Исходный размер:', len(chisla))

with open('output3.bin', 'wb') as file:
    for i in range(2):
        for i in range(len(chisla)):
            pickle.dump(chisla[i], file)

print('\nДанные из файла:')
with open('output3.bin', 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except Exception as e:
            break