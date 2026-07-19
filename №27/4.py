'''TreeWork55. Дан текстовый файл, в первой строке которого записана последовательность неповторяющихся целых чисел. Числа разделены
пробелами. Необходимо построить из этих чисел дерево поиска и вывести корень дерева, а также содержимое дерева, используя концевой
обход.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self.insert_2(value, self.root)

    def insert_2(self, value, root):
        if value < root.value:
            if not root.left:
                root.left = Node(value)
            else:
                self.insert_2(value, root.left)
        else:
            if not root.right:
                root.right = Node(value)
            else:
                self.insert_2(value, root.right)

    def inoder(self, root):
        if root:
            self.inoder(root.left)
            print(root.value)
            self.inoder(root.right)

with open('input4.txt', 'r') as file:
    numbers = map(int, file.readline().split())

tree = BinaryTree()
for i in numbers:
    tree.insert(i)

print(tree.root.value)
tree.inoder(tree.root)
