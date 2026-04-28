'''ListWork8. Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вывести указатель на девятый элемент этого списка P9. Известно,
что в исходном списке не менее 9 элементов.'''

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

spicok = Node(10)
for i in range(9, 0, -1):
    spicok = Node(i, spicok)

for i in range(8):
    spicok = spicok.next

print(spicok)