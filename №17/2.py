'''Dynamic53. Даны ссылки AX и AY на два различных элемента двусвязного списка; элемент AX находится в списке перед элементом AY,
но не обязательно рядом с ним. Переместить элементы, расположенные между данными элементами (включая данные элементы), в новый список
(в том же порядке). Вывести ссылки на первые элементы преобразованного и нового списков. Если преобразованный список окажется пустым,
то связанную с ним ссылку положить равной null. Новые объекты типа Node не создавать. '''

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

        return new_node

    def delete(self, link):
        if self.head is None:
            return 'Error'
        else:
            curr = self.head
            while curr != self.tail and curr != link:
                curr = curr.next

            if curr == link:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next = None
                curr.prev = None

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

old_spic = DoublyLinkedList()
print('Ссылки на выбор:')
for i in range(1,11):
    print(old_spic.append(i))

ax = input('\nВведите AX (ссылку): ')
ay = input('Введите AY (ссылку): ')
curr = old_spic.head

new_spic = DoublyLinkedList()
flag = False
while curr is not None:
    if str(curr) == ax:
        flag = True
        new_spic.append(curr.data)
        curr = curr.next
        old_spic.delete(curr.prev)

    elif str(curr) == ay:
        new_spic.append(curr.data)
        old_spic.delete(curr)
        break

    elif flag == True:
        new_spic.append(curr.data)
        curr = curr.next
        old_spic.delete(curr.prev)

    else:
        curr = curr.next

print(old_spic.print_forward())
print(new_spic.print_forward())

print(old_spic.head)
if new_spic.head is None:
    print('null')
else:
    print(new_spic.head)