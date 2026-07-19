'''TreeWork27. Дано дерево поиска и корень дерева P1. Удалить в дереве корневую вершину. При замене содержимого удаляемой вершины использовать данные
из ее правого поддерева. После удаления вывести строку с описанием исходного дерева в следующем формате: <дерево>::=((<левое поддерево>)<вершина>
(<правое поддерево>)) | ((<левоеподдерево>)<вершина>) | (<вершина>(<правое поддерево>)) <вершина>::=<цифра><цифра>|<цифра> <левое поддерево>::=<дерево>
<правое поддерево>::=<дерево> Например, "(((1)2((3)4))5(6(7)))". Пробелы в результирующей строке отсутствуют, ссылки на пустые деревья никак не выводятся.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def delete_root(self):
        if self.root is None:
            return
        if self.root.left is None and self.root.right is None:
            self.root = None
            return
        if self.root.right is not None:
            parent = self.root
            successor = self.root.right
            while successor.left is not None:
                parent = successor
                successor = successor.left
            self.root.value = successor.value
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right
        else:
            self.root = self.root.left

    def to_string(self, node):
        if node is None:
            return ""
        left = self.to_string(node.left)
        right = self.to_string(node.right)
        val = str(node.value)
        if not left and not right:
            return f"({val})"
        if left and not right:
            return f"({left}{val})"
        if not left and right:
            return f"({val}{right})"
        return f"({left}{val}{right})"

tree = BinaryTree()
tree.root = Node(5)
tree.root.left = Node(2)
tree.root.left.left = Node(1)
tree.root.left.right = Node(4)
tree.root.left.right.left = Node(3)
tree.root.right = Node(6)
tree.root.right.right = Node(7)

tree.delete_root()
print(tree.to_string(tree.root))