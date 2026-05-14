'''TreeWork8. Дан корень P1 непустого дерева. Вывести значения всех вершин дерева в инфиксном порядке
(вначале выводится содержимое левого поддерева в инфиксном порядке,затем выводится значение корня,
затем — содержимое правого поддерева в инфиксном порядке).'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

tree = BinaryTree()
tree.root = Node(5)
tree.root.left = Node(3)
tree.root.right = Node(7)
tree.root.left.left = Node(2)
tree.root.left.right = Node(4)
tree.root.right.left = Node(6)
tree.root.right.right = Node(8)

tree.inorder(tree.root)