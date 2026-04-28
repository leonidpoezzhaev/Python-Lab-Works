'''Strat31. Петя и Вася играют в игру на клетчатой доске n×n. Изначально вся доска белая, за исключением угловой
клетки — она чёрная, и в ней стоит ладья. Игроки ходят по очереди. Каждым ходом игрок передвигает ладью по
горизонтали или вертикали, при этом все клетки,через которые ладья перемещается (включая ту, в которую она
попадает), перекрашиваются в чёрный цвет. Ладья не должна передвигаться через чёрные клетки или останавливаться
на них.Проигрывает тот, кто не может сделать ход.'''

import random

class Board:
    def __init__(self, n):
        self.n = n
        self.grid = [[False for _ in range(n)] for _ in range(n)]
        self.rook_pos = (0, 0)
        self.grid[0][0] = True

    def is_black(self, x, y):
        return self.grid[x][y]

    def set_black(self, x, y):
        self.grid[x][y] = True

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def get_possible_moves(self):
        x, y = self.rook_pos
        moves = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            while self.is_valid(nx, ny):
                if self.is_black(nx, ny):
                    break
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return moves

    def apply_move(self, new_pos):
        x1, y1 = self.rook_pos
        x2, y2 = new_pos
        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step):
                self.set_black(x1, y)
        elif y1 == y2:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step):
                self.set_black(x, y1)
        else:
            raise ValueError("Invalid move")
        self.rook_pos = new_pos

    def display(self):
        print("  " + " ".join(str(i) for i in range(self.n)))
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if (i, j) == self.rook_pos:
                    row.append('R')
                elif self.grid[i][j]:
                    row.append('#')
                else:
                    row.append('.')
            print(f"{i} " + " ".join(row))
        print()

class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def make_move(self, board):
        moves = board.get_possible_moves()
        if not moves:
            return None
        while True:
            try:
                inp = input(f"{self.name}, введите координаты хода (строка столбец): ")
                x, y = map(int, inp.split())
                if (x, y) in moves:
                    return (x, y)
                else:
                    print("Недопустимый ход. Попробуйте снова.")
            except:
                print("Ошибка ввода. Введите два целых числа через пробел.")

class ComputerPlayer(Player):
    def make_move(self, board):
        moves = board.get_possible_moves()
        if not moves:
            return None
        move = random.choice(moves)
        print(f"Компьютер {self.name} ходит на {move}")
        return move

class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        while True:
            self.board.display()
            current = self.players[self.current_player_index]
            print(f"Ход игрока: {current.name}")
            moves = self.board.get_possible_moves()
            if not moves:
                print(f"Игрок {current.name} не может сделать ход. Он проигрывает.")
                winner = self.players[(self.current_player_index + 1) % len(self.players)]
                print(f"Победитель: {winner.name}!")
                break
            move = current.make_move(self.board)
            if move is None:
                print("Нет доступных ходов, игра завершена.")
                break
            self.board.apply_move(move)
            self.switch_player()

def main():
    print("Добро пожаловать в игру Ладья!")
    n = int(input("Введите размер доски n (2-10): "))
    if n < 2:
        n = 2
    if n > 10:
        n = 10
    mode = input("Выберите режим: 1 - игра против компьютера, 2 - два человека: ")
    board = Board(n)
    players = []
    if mode == "1":
        players.append(HumanPlayer("Игрок"))
        players.append(ComputerPlayer("Компьютер"))
    else:
        players.append(HumanPlayer("Игрок 1"))
        players.append(HumanPlayer("Игрок 2"))
    game = Game(players, board)
    game.play()

if __name__ == "__main__":
    main()