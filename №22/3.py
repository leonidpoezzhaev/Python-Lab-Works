'''Graf9. Юный путешественник решил изучить схему авиационного сообщения. Схема авиационного сообщения задана в текстовом файле
с именем FileName3_1 в виде матрицы смежности. Первая строка файла содержит количество городов (n) n<=15, связанных авиационным
сообщением, а следующие n строк хранят матрицу (m), m[i][j] = 0, если не имеется возможности перелета из города i в город j,
иначе m[i][j]=1. Определить сколько есть маршрутов из города К1 в город К2 с L пересадками. В файл с именем FileName3_2 в
первой строке выведите число таких маршрутов, а в следующих строках перечислите все такие маршруты в лексикографическом порядке.
Маршрут задается перечислением номеров городов, нумерация городов идет с 1. Если таких маршрутов нет, выведите число (-1).'''

def dfs(u, path):
    if len(path) == target_len:
        if u == end:
            routes.append(path[:])
        return
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            path.append(v)
            dfs(v, path)
            path.pop()
            visited[v] = False

with open('FileName3_1.txt', 'r') as f:
    tokens = f.read().split()

n = int(tokens[0])
idx = 1
adj = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if int(tokens[idx]) == 1:
            adj[i].append(j)
        idx += 1

K1 = int(tokens[idx])
K2 = int(tokens[idx + 1])
L = int(tokens[idx + 2])
start = K1 - 1
end = K2 - 1
target_len = L + 2
routes = []
visited = [False] * n
visited[start] = True
dfs(start, [start])

with open('FileName3_2.txt', 'w') as f:
    if not routes:
        f.write('-1')
    else:
        f.write(str(len(routes)) + '\n')
        for route in routes:
            f.write(' '.join(str(x + 1) for x in route) + '\n')