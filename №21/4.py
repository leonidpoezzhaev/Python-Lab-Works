'''SimpleIter1. Написать класс, реализующий интерфейс итератора. Класс должен принимать в конструкторе
список элементов произвольного типа и позволять просмотреть его в обратном порядке.'''

class SimpleIter1:
    def __init__(self, lst):
        self._lst = lst
        self._index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        value = self._lst[self._index]
        self._index -= 1
        return value

for item in SimpleIter1([10, 20, 30, 40]):
        print(item)