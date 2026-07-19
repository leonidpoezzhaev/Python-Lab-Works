'''TreeFun4. Реализовать для бинарного дерева интерфейс итератора, который будет возвращать значения элементов, находящихся в узлах дерева, в порядке
"право-корень-лево". Преобразовывать дерево в список или иную структуру данных нельзя, рекурсию использовать запрещается.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.right
            current = stack.pop()
            yield current.value
            current = current.left

tree = BinaryTree()
tree.root = Node(1)
tree.root.right = Node(2)
tree.root.left = Node(3)
tree.root.right.right = Node(4)
tree.root.right.left = Node(5)
tree.root.left.right = Node(6)
tree.root.left.left = Node(7)

for val in tree:
    print(val)