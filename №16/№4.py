'''ListWork25. Дан односвязный линейный список и указатель на голову списка P1. Необходимо вставить значение M
перед каждым вторым элементом списка, и вывести ссылку на последний элемент полученного списка P2. При нечетном
числе элементов исходного списка в конец списка вставлять не надо.'''

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

spicok = Node(10)
for i in range(9, 0, -1):
    spicok = Node(i, spicok)

m = int(input('Введите значение M: '))

elements = []
for i in range(1,11):
    elements.append(spicok.data)
    spicok = spicok.next
    if i % 2 == 0:
        elements.append(m)

spicok = Node(elements[-1])
print(spicok)

elements = elements[::-1]
for i in elements[1:]:
    spicok = Node(i, spicok)