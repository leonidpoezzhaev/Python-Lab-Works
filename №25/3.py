'''Shifr1. Написать программу для шифрования и дешифрования последовательности символов шифром Цезаря.'''

def encrypt(text, key):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    new_text = ''
    for i in text:
        new_text += alphabet[alphabet.find(i)+key]
    return new_text

def decrypt(text, key):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    new_text = ''
    for i in text:
        new_text += alphabet[alphabet.find(i)-key]
    return new_text

text = input('Введите текст: ')
key = int(input('Введите ключ (на сколько сдвигаются символы): '))

encoded_text = encrypt(text, key)
print('Закодированный текст:', encoded_text)

decoded_text = decrypt(encoded_text, key)
print('Декодированный текст:', decoded_text)