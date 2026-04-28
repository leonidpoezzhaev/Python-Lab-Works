'''BackTrack14. Задача вывода путника из лабиринта. Дан лабиринт размером NхN (N<=15). Форма лабиринта записана
в текстовом файле, стена обозначается символом М, отсутствие стены - символом пробела. Даны координаты мышки в
лабиринте (номер строки (X) и номер столбца (Y)) и координаты сыра (номер строки (XС) и номер столбца (YС)).
Нужно вывести самый короткий путь мышки к сыру. Для этого распечатать сам лабиринт и обозначить путь
символами +. Гарантируется, что такой путь только один. Длина пути определяется числом клеток, на которые
должна ступить нога мышки'''

def shortest_path(maze, x, y, xc, yc, visited):
    if x == xc and y == yc:
        return [(x, y)]
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    best = None
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] != 'M' and not visited[nx][ny]:
                sub = shortest_path(maze, nx, ny, xc, yc, visited)
                if sub is not None:
                    if best is None or len(sub) < len(best):
                        best = sub
    visited[x][y] = False
    if best is not None:
        return [(x, y)] + best
    return None

def main():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    if not data:
        return
    N = int(data[0].strip())
    X, Y = map(int, data[1].split())
    XC, YC = map(int, data[2].split())
    maze = []
    for i in range(3, 3 + N):
        row = list(data[i].rstrip('\n'))
        if len(row) < N:
            row.extend([' '] * (N - len(row)))
        maze.append(row[:N])
    start_row = X - 1
    start_col = Y - 1
    cheese_row = XC - 1
    cheese_col = YC - 1
    visited = [[False] * N for _ in range(N)]
    path = shortest_path(maze, start_row, start_col, cheese_row, cheese_col, visited)
    if path is None:
        print("No path found")
        return
    for r, c in path:
        maze[r][c] = '+'
    for row in maze:
        print(''.join(row))

if __name__ == '__main__':
    main()