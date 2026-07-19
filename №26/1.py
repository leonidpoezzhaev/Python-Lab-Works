'''CalcTree8. В текстовом файле с именем filename дано арифметическое выражение в префиксной форме. Операндами в выражении являются целые числа из промежутка
от 0 до 9. Используемые операции: сложение (+), вычитание (-), умножение (*), деление нацело(/), целочисленный остаток от деления (%) и возведение встепень (^).
Постройте дерево, соответствующее данному выражению. Знаки операций кодируйте числами: сложение(-1), вычитание (-2), умножение (-3), деление (-4),
остаток от деления (-5), возведение встепень(-6). Преобразуйте дерево, вычислив значения всех поддеревьев, для которых результат вычислений левого или правого
поддерева равен нулю (замените такие поддеревья их значениями). Выведите указатель на корень полученного дерева.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class CalcTree:
    def __init__(self):
        self.root = None

    def build(self, expr):
        ops = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6}
        tokens = expr.split()

        def parse(i):
            token = tokens[i]
            if token in ops:
                node = Node(ops[token])
                node.left, i = parse(i + 1)
                node.right, i = parse(i)
                return node, i
            else:
                return Node(int(token)), i + 1

        self.root, _ = parse(0)

    def transform(self):
        def evaluate(node):
            if node.value >= 0:
                return node.value
            left_val = evaluate(node.left)
            right_val = evaluate(node.right)
            op = node.value
            if op == -1:
                return left_val + right_val
            elif op == -2:
                return left_val - right_val
            elif op == -3:
                return left_val * right_val
            elif op == -4:
                return left_val // right_val
            elif op == -5:
                return left_val % right_val
            elif op == -6:
                return left_val ** right_val

        def dfs(node):
            if node.value >= 0:
                return
            dfs(node.left)
            dfs(node.right)
            left_val = evaluate(node.left)
            right_val = evaluate(node.right)
            if left_val == 0 or right_val == 0:
                res = evaluate(node)
                node.value = res
                node.left = None
                node.right = None

        dfs(self.root)


with open('filename.txt', 'r') as f:
    expr = f.read().strip()

tree = CalcTree()
tree.build(expr)
tree.transform()
print(tree.root)