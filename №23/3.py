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
        max1 = None
        max2 = None
        stack = [self.root]
        while stack:
            node = stack.pop()
            if max1 is None or node.value > max1:
                max2 = max1
                max1 = node.value
            elif node.value != max1 and (max2 is None or node.value > max2):
                max2 = node.value
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return max2

tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(20)
tree.root.right = Node(30)
tree.root.left.left = Node(40)
tree.root.left.right = Node(50)
tree.root.right.left = Node(60)

print(tree.find_second_max())