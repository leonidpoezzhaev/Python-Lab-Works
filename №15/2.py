'''2. Имеется информация об учениках младшей школы. Для всех учеников известны: фамилия, имя и класс.
Для учеников 1-х классов дополнительно известна их скорость чтения(слов в минуту, тип int).
Для учеников 4-х классов известны баллы итоговой аттестации (единый муниципальный тест от 1 до 100 баллов, тип float).
Для учеников 2-х и 3-х классов известны данные итоговой школьной контрольной по математике (оценки от 1 до 10 баллов,тип float).
Написать функцию, позволяющую ввести с клавиатуры данные для одного ученика. Используя эту функцию,
ввести сведения об N учениках и сохранить их в бинарном файле.Распечатать на экране содержимое данного файла в виде таблицы.'''
import pickle

class Students:
    def __init__(self, name, surname, klass, other):
        self.name = name
        self.surname = surname
        self.klass = klass
        self.other = other

    def __str__(self):
        return f'{self.name} {self.surname} {self.klass} {self.other}'

def main():
    n = int(input('Введите количество учеников: '))
    with open('output2.bin', 'wb') as file:
        for i in range(n):
            name, surname, klass, other = input('Введите данные о ученике: ').split()
            s = Students(name, surname, klass, other)
            pickle.dump(str(s), file)

    with open('output2.bin', 'rb') as file:
        print('Фамилия Имя Класс Доп.Данные')
        while True:
            try:
                print(pickle.load(file))
            except Exception as e:
                break

if __name__ == '__main__':
    main()