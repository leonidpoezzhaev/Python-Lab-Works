'''TreeFun2. Преобразовать двусвязный список в бинарное дерево поиска без использования дополнительной памяти (создания новых объектов).
Корнем дерева должен стать элемент списка, находящийся в его середине, а само дерево должно иметь наименьшую возможную высоту. При
преобразовании поля left и right узлов бинарного дерева рассматриваются эквивалентными полям prev и next узлов двусвязного списка.
Вывести исходный список и получившееся дерево.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(' '.join(values))

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_dll(self, dll):
        if not dll.head:
            return
        n = 0
        cur = dll.head
        while cur:
            n += 1
            cur = cur.next
        head_ref = [dll.head]
        self.root = self.sorted(head_ref, n)

    def sorted(self, head_ref, n):
        if n <= 0:
            return None
        left = self.sorted(head_ref, n // 2)
        root = head_ref[0]
        head_ref[0] = root.next
        root.prev = left
        root.next = self.sorted(head_ref, n - n // 2 - 1)
        return root

    def display(self): #
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.prev
            current = stack.pop()
            print(current.value, end=' ')
            current = current.next

dll = DoublyLinkedList()
for v in [1, 2, 3, 4, 5, 6, 7]:
    dll.append(v)

print("Исходный список:")
dll.display()

bt = BinaryTree()
bt.build_dll(dll)

print("\nБинарное дерево поиска (симметричный обход):")
bt.display()