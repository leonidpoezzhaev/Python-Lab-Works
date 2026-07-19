'''TreeWork66. В первой строке текстового файла записаны целые числа, разделенные пробелами. Создать дерево поиска, последовательно включая в него
перечисленные в файле числа. После этого необходимо, привести дерево к АВЛ-сбалансированному виду, выполнив для LR-поворот. Известно, что требуется
не более одного такого поворота. Вывести корень полученного дерева.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                cur = cur.right

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    return y

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    return y

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def balance_tree(node):
    if node is None:
        return node
    node.left = balance_tree(node.left)
    node.right = balance_tree(node.right)
    bal = height(node.left) - height(node.right)
    if bal > 1:
        left_bal = height(node.left.left) - height(node.left.right)
        if left_bal < 0:
            node.left = left_rotate(node.left)
            return right_rotate(node)
    return node

with open('input3.txt') as f:
    data = f.read().split()

tree = BinaryTree()
for num in data:
    tree.insert(int(num))

tree.root = balance_tree(tree.root)
print(tree.root.value)