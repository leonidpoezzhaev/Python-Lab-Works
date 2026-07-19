'''TreeWork66. В первой строке текстового файла записаны целые числа, разделенные пробелами. Создать дерево поиска, последовательно
включая в него перечисленные в файле числа. После этого необходимо, привести дерево к АВЛ-сбалансированному виду, выполнив для LR-поворот.
Известно, что требуется не более одного такого поворота. Вывести корень полученного дерева.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class CalcTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(value)
                    break
            elif value > cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(value)
                    break
            else:
                break

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def find_imbalance(self):
        def dfs(node, parent):
            if node is None:
                return None, None
            lh = self.height(node.left)
            rh = self.height(node.right)
            if lh - rh > 1:
                left = node.left
                if self.height(left.right) > self.height(left.left):
                    return node, parent
            left_res = dfs(node.left, node)
            if left_res[0]:
                return left_res
            return dfs(node.right, node)
        return dfs(self.root, None)

    def lr_rotate(self, a):
        b = a.left
        c = b.right
        b.right = c.left
        c.left = b
        a.left = c.right
        c.right = a
        return c

    def balance(self):
        a, parent = self.find_imbalance()
        if a is None:
            return
        new_sub = self.lr_rotate(a)
        if parent is None:
            self.root = new_sub
        elif parent.left == a:
            parent.left = new_sub
        else:
            parent.right = new_sub

tree = CalcTree()
with open('input.txt') as f:
    for num in f.readline().split():
        tree.insert(int(num))

tree.balance()
print(tree.root.value)