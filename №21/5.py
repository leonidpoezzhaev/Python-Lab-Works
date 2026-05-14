'''CalcIter1. Расширить класс односвязного списка из лабораторной работы №15 интерфейсом итератора. По достижении конца
списка итератор должен начать возвращать элементы в обратном порядке, а затем — по достижении начала — снова в прямом.'''

class Node:
    __slots__ = ('data', 'next')
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def __iter__(self):
        return self._PingPongIterator(self.head)

    class _PingPongIterator:
        def __init__(self, head):
            self._head = head
            self._cur = head
            self._nodes = []
            self._idx = 0
            self._state = 'forward'

        def __iter__(self):
            return self

        def __next__(self):
            while True:
                if self._state == 'forward':
                    if self._cur is not None:
                        val = self._cur.data
                        self._nodes.append(self._cur)
                        self._cur = self._cur.next
                        return val
                    else:
                        if not self._nodes:
                            raise StopIteration
                        self._state = 'backward'
                        self._idx = len(self._nodes) - 1
                elif self._state == 'backward':
                    if self._idx >= 0:
                        val = self._nodes[self._idx].data
                        self._idx -= 1
                        return val
                    else:
                        self._state = 'forward'
                        self._cur = self._head

lst = LinkedList()
for ch in ['A', 'B', 'C']:
    lst.append(ch)

it = iter(lst)
for _ in range(9):
    print(next(it))