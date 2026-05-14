'''TreeWork18. Дано бинарное дерево и корень дерева P1. Необходимо вывести второе максимальное значение в дереве.
Решение должно иметь сложность по времени исполнения T(n) = O(log n), где n - число вершин в дереве.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def find_second_max(self):
        if self.root is None:
            return None
        parent = None
        current = self.root
        while current.right is not None:
            parent = current
            current = current.right
        if current.left is not None:
            current = current.left
            while current.right is not None:
                current = current.right
            return current.value
        if parent is not None:
            return parent.value
        return None

tree = BinaryTree()
tree.root = Node(50)
tree.root.left = Node(30)
tree.root.right = Node(70)
tree.root.left.left = Node(20)
tree.root.left.right = Node(40)
tree.root.right.left = Node(60)
tree.root.right.right = Node(80)

print(tree.find_second_max())