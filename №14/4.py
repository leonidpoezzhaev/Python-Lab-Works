'''File55. Дана строка S0, целое число N (≤ 4) и N файлов целых чисел с именамиS1, …, SN.
Объединить их содержимое в новом файле-архиве с именем S0, последовательно записывая в него следующие данные:
размер (число элементов) первого исходного файла и все элементы этого файла,
размер второго исходного файла и все его элементы, …, размер N-го исходног офайла и все его элементы.'''

import pickle

s0 = input('Введите строку S0 (название файла): ')
n = int(input('Введите количество файлов: '))
chisla = []
for i in range(1,n+1):
    chis = []
    with open(f'input4_{i}.bin', 'rb') as f:
        while True:
            try:
                chis.append(pickle.load(f))
            except Exception as e:
                break
    print(f'\nЭлементы {i} файла:',*chis)
    print('Размер:', len(chis))
    chisla.append(f'Размер: {len(chis)}')
    chisla.extend(chis)

with open(f'{s0}.bin', 'wb') as file:
    for i in range(len(chisla)):
        pickle.dump(chisla[i], file)

print('\nДанные из файла:')
with open(f'{s0}.bin', 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except Exception as e:
            break