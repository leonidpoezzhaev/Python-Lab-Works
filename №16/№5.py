'''ListWork62. Дан текстовый файл в первой строке которого хранится число N, а во второй строке N целых чисел.
Необходимо создать упорядоченный по убыванию список, в который поместить все эти элементы, при этом очередной
элемент вставлять в список так, чтобы не нарушалась его упорядоченность.'''

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

with open('input5.txt', 'r') as f:
    n = int(f.readline().strip())
    chisla = list(map(int, f.readline().strip().split()))

chisla.sort(reverse=True)

spicok = Node(chisla[0])
for i in chisla[1:]:
    spicok = Node(i, spicok)