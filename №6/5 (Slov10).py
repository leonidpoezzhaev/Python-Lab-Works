'''Slov10. Напишите программу, которая принимает на вход две строки и
определяет, являются ли они анаграммами (cлово или словосочетание,
образованное путём перестановки букв, составляющих другое слово (или
словосочетание)). Знаки препинания, пробелы и регистр при этом
игнорируются.'''
def func(strok):
    spic = []
    bykvi = {}
    for i in strok:
        spic.append(i)
    spic = list(set(spic))
    try:
        spic.remove(' ')
    except ValueError:
        None
    for i in spic:
        bykvi[i] = strok.count(i)
    return bykvi

str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
if func(str1) == func(str2):
    print('Это анаграммы!')
else:
    print('Это не анаграммы :(')
