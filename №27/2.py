'''TreeWork40. Дан корень дерева, хранящего арифметическое выражение. В выражении участвуют неотрицательные однозначные целые числа, знаки операций
кодируются отрицательными числами: сложению соответствует -1, вычитанию -2, умножению -3, делению -4. Определить, возникнет ли ошибка "Деление на ноль!"
при вычислении данного выражения. Вывести True, если это так, и False в противном случае.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def _evaluate(self, node):
        if node.value >= 0:
            return node.value, False
        left_val, left_err = self._evaluate(node.left)
        if left_err:
            return 0, True
        right_val, right_err = self._evaluate(node.right)
        if right_err:
            return 0, True
        op = node.value
        if op == -1:
            return left_val + right_val, False
        elif op == -2:
            return left_val - right_val, False
        elif op == -3:
            return left_val * right_val, False
        elif op == -4:
            if right_val == 0:
                return 0, True
            return left_val // right_val, False
        else:
            return 0, True

    def division_by_zero(self):
        if self.root is None:
            return False
        _, error = self._evaluate(self.root)
        return error


tree = BinaryTree()
node_plus = Node(-1)
node_div = Node(-4)
node_5 = Node(5)
node_0 = Node(0)
node_3 = Node(3)

node_div.left = node_5
node_div.right = node_0
node_plus.left = node_div
node_plus.right = node_3
tree.root = node_plus

print(tree.division_by_zero())

tree2 = BinaryTree()
node_mul = Node(-3)
node_3b = Node(3)
node_plus2 = Node(-1)
node_2 = Node(2)
node_1 = Node(1)

node_plus2.left = node_2
node_plus2.right = node_1
node_mul.left = node_3b
node_mul.right = node_plus2
tree2.root = node_mul

print(tree2.division_by_zero())