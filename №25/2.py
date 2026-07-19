'''Для данного текста написать программу с кодом Хаффмана. Для каждого символадолженбыть указан его код, а также должно
быть приведено дерево кодирования выполненное в «вручную». Вычислить размер сообщения при равномерном кодировании и
прикодировании с помощью построенного кода Хаффмана.
Текст: У ЁЛКИ ИГОЛКИ КОЛКИ'''

from huffman import Huffman
from math import ceil, log

text = 'У ЁЛКИ ИГОЛКИ КОЛКИ'
len_text = len(text)

chastoti = Huffman.get_letters_frequency(text)
chastoti = dict(sorted(chastoti.items(), key=lambda item: -item[1]))

print('--ЧАСТОТЫ--')
for i in chastoti:
    chastoti[i] = chastoti[i] / len_text
    print(i, chastoti[i])

print('\n--КОДЫ--')
code_simvols = Huffman.generate_dictionary(text)
for i in code_simvols:
    print(i, code_simvols[i])

L = 0
for i in code_simvols:
    L += len(code_simvols[i]) * chastoti[i]

print('\n--УДЛИНЕНИЕ--')
print('Lхф =', L)
print('Длина закодированного Хаффманом текста:', L*len(text))

Lrm = ceil(log(len(chastoti), 2))
print('\nLрм =', Lrm)
print('Длина равномерного закодированного текста:', Lrm*len(text))

code_text = ''
for i in text:
    code_text += code_simvols[i]

print('\nЗакодированное сообщение:')
print(code_text)