'''Dynamic10. Дана вершина A1 непустого стека. Создать два новых стека, переместив в первый из них все элементы исходного стека
с четными значениями, а во второй — с нечетными(элементы в новых стеках будут располагаться в порядке, обратном исходному;
один из этих стеков может оказаться пустым). Вывести ссылки на вершины полученных стеков(для пустого стека вывести константу null). Новые объекты типа Node не создавать.'''

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

stack1 = Node(1)
for i in range(2,11):
    stack1 = Node(i, stack1)

stack2 = Node(999)
stack3 = Node(999)

for i in range(len(stack1)):
    if stack1.data % 2 == 0:
        if stack2.data == 999:
            stack2 = Node(stack1.data)
        else:
            stack2 = Node(stack1.data, stack2)
    else:
        if stack2.data == 999:
            stack3 = Node(stack1.data)
        else:
            stack3 = Node(stack1.data, stack3)

    stack1 = stack1.next

print(stack2.data, stack2.next.data)
print(stack3.data, stack3.next.data)