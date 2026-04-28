'''File27. Дан файл целых чисел с элементами A1, A2, …, AN (N —количество элементов в файле).
Заменить исходное расположение его элементов на следующее:
A1, AN, A2, AN−1, A3, …'''

import pickle

chisla = []
with open('input2.bin', 'rb') as f:
    while True:
        try:
            chisla.append(pickle.load(f))
        except Exception as e:
            break

print('Исходные элементы:', *chisla)
print('Кол-во элементов:', len(chisla))

new_chisla = []
for i in range(len(chisla)//2):
    new_chisla.append(chisla[i])
    new_chisla.append(chisla[len(chisla)-1-i])

with open('output2.bin', 'wb') as file:
    for i in range(len(new_chisla)):
        pickle.dump(new_chisla[i], file)

print('\nДанные из файла:')
with open('output2.bin', 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except Exception as e:
            break