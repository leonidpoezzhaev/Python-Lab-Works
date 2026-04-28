'''Dynamic77. Даны ссылки A1 и A2 на барьерный и текущий элементы двусвязного списка.Также даны пять чисел.Включить в класс IntListB
(см. задание Dynamic74) процедуру InsertAfter(D), которая вставляет новый элемент со значением D после текущего элемент асписка
(D — входной параметр целого типа). Вставленный элемент становится текущим. С помощью метода InsertAfter вставить пять данных чисел
в исходный список и вывести ссылку на текущий элемент полученного списка.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def PT_put(x):
    return "null" if x is None else repr(x)

class IntListB:
    def __init__(self):
        self.current = None
        self.barrier = Node(0)

    def InsertLast(self, D):
        new_node = Node(D)
        if self.current is None:
            new_node.prev = self.barrier
            new_node.next = self.barrier
            self.barrier.next = new_node
            self.barrier.prev = new_node
            self.current = new_node
        else:
            self.current.next = new_node
            new_node.prev = self.current
            new_node.next = self.barrier
            self.barrier.prev = new_node

    def Put(self):
        print(PT_put(self.current))

    def InsertAfter(self, D):
        new_node = Node(D)
        if self.current is None:
            new_node.prev = self.barrier
            new_node.next = self.barrier
            self.barrier.next = new_node
            self.barrier.prev = new_node
            self.current = new_node
        else:
            self.current.next = new_node
            new_node.prev = self.current
            new_node.next = self.barrier
            self.barrier.prev = new_node

original = IntListB()
for i in range(1,6):
    original.InsertAfter(i)

for i in range(5):
    original.InsertAfter(int(input(f'Введите {i+1} целое число для добавления в список: ')))

print(original.current)
