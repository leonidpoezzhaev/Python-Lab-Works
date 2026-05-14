'''Graf7. Две корпорации хотят разделить сферы влияния, выбрав два разных города для размещения своих штаб-квартир
так, чтобы все города, в некоторой округе от штаб-квартиры не были доступны для конкурентов. Схема автомобильного
сообщения между городами задана в текстовом файле с именем FileName2 в виде матрицы смежности. Первая строка файла
содержит количество городов (n, n<=25), связанных дорогами, а следующие n строк хранят матрицу (m), m[i][j]=0,
если нет дороги из города i в город j, иначе m[i][j] = 1. Даны два города-кандидата с номерами K1 и K2 для этих
двух штаб-квартир. Определить есть ли города, в которые можно попасть из обоих штаб-квартир, если двигаться от
каждой штаб-квартиры не более чем через L промежуточных городов. Перечислите номера таких городов в порядке
возрастания. Нумерация городов начинается с 1. Если таких городов нет, выведите число (-1).'''

def reachable(start, max_depth):
    visited = set()
    queue = [(start, 0)]
    visited.add(start)
    while queue:
        v, d = queue.pop(0)
        if d == max_depth:
            continue
        for u, has_edge in enumerate(adj[v]):
            if has_edge and u not in visited:
                visited.add(u)
                queue.append((u, d + 1))
    return visited

data = open('FileName2.txt').read().split()
n = int(data[0])
idx = 1
adj = []

for i in range(n):
    row = [int(x) for x in data[idx:idx+n]]
    adj.append(row)
    idx += n

K1, K2, L = map(int, data[idx:idx+3])
K1 -= 1
K2 -= 1
set1 = reachable(K1, L + 1)
set2 = reachable(K2, L + 1)
common = sorted(set1 & set2)

if common:
    print(*[c + 1 for c in common])
else:
    print(-1)