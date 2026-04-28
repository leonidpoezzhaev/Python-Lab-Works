'''Dynamic66. Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы непустого двусвязного списка. Включить в класс IntList
(см. задание Dynamic59) классовый метод—процедуру Split(L1, L2), которая переносит элементы списка L1 от текущего до последнего в новый
список L2 (таким образом, список L1 делится на две части, причем первая часть может оказаться пустой). Параметры процедуры имеют тип IntList;
первый параметр является входным, второй — выходным. Текущими элементами непустых результирующих списков становятся их первые элементы.
Новые объекты типа Node в процедуре Split не создавать. Спомощью этой процедуры разбить исходный список на два и вывести ссылки на первый,
последний и текущий элементы каждого из полученных списков (для пустого списка выводятся три константы null).'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def PT_put(x):
    return "null" if x is None else repr(x)

class IntList:
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None

    def InsertLast(self, D):
        new_node = Node(D)
        if self.first is None:
            self.first = self.last = self.current = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
            self.current = new_node

    def Put(self):
        print(PT_put(self.first), PT_put(self.last), PT_put(self.current))

    @classmethod
    def Split(cls, L1, L2):
        if L1.first is None:
            return

        split_node = L1.current
        L2.first = split_node
        L2.last = L1.last
        L2.current = split_node
        left_tail = split_node.prev

        if left_tail is None:
            L1.first = L1.last = L1.current = None
        else:
            left_tail.next = None
            L1.last = left_tail
            L1.current = L1.first

            if L1.first is None:
                L1.last = L1.current = None

        split_node.prev = None

a = IntList()
for i in range(1,11):
    a.InsertLast(i)

b = IntList()

IntList.Split(a,b)

print(a.first, a.last, a.current)

print(b.first, b.last, b.current)