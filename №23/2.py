'''TreeWork10. Дано бинарное дерево и корень дерева P1. Необходимо вставить в дерево значение X.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = Node(x)
                return
            queue.append(current.left)
            if current.right is None:
                current.right = Node(x)
                return
            queue.append(current.right)

tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(20)
tree.root.right = Node(30)
tree.root.left.left = Node(40)
tree.root.left.right = Node(50)
tree.root.right.left = Node(60)

X = 70
tree.insert(X)