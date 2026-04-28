'''Dynamic38. Дан первый элемент A1 непустого двусвязного списка. Продублировать в списке все элементы с нечетными
номерами (новые элементы добавлять после существующих элементов с такими же значениями) и вывести ссылку на последний
элемент преобразованного списка.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

old_spic = DoublyLinkedList()
for i in range(1,6):
    old_spic.append(i)

new_spic = DoublyLinkedList()
curr = old_spic.head
while curr is not None:
    new_spic.append(curr.data)
    if curr.data % 2 != 0:
        new_spic.append(curr.data)
    curr = curr.next

new_spic.print_forward()