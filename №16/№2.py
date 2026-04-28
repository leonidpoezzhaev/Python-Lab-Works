'''Dynamic17. Дано число D и ссылки A1 и A2 на начало и конец очереди (если очередь является пустой, то A1 = A2 = null).
Добавить элемент со значением D в конец очереди и вывести ссылки на начало и конец полученной очереди.'''

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __len__(self):
        a = self.next
        countt = 1
        while a != None:
            a = a.next
            countt += 1
        return countt

quque = Node(1)
for i in range(2,6):
    quque = Node(i, quque)

d = int(input('Введите D: '))
quque = Node(d, quque)

a = quque
while a.next != None:
    a = a.next
print(a)

print(quque)


