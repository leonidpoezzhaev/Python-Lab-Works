'''Strat9. Петя и Коля играют в такую игру. Петя загадывает натуральное число от 1 до 2012. Коля называет натуральные числа,
и после каждого названного числа Петя говорит «недобор», если названное число меньше загаданного, и «перебор», если названное
число больше загаданного. Если названное число совпадает с загаданным, то Петя говорит «угадал» и игра заканчивается победой Коли.
При этом если в процессе отгадывания дважды возник «перебор», то игра заканчивается победой Пети.'''
import random

class Petia:
    pass

class PetiaHuman(Petia):
    def __init__(self):
        while True:
            try:
                self.secret = int(input("Игрок Петя, загадайте натуральное число от 1 до 2012: "))
                if 1 <= self.secret <= 2012:
                    break
                else:
                    print("Число должно быть от 1 до 2012.")
            except ValueError:
                print("Введите целое число.")
        self.over_count = 0
        self.game_over = False
        self.winner = None

    def check(self, guess):
        if guess == self.secret:
            self.game_over = True
            self.winner = "Коля"
            return "угадал"
        elif guess < self.secret:
            return "недобор"
        else:
            self.over_count += 1
            if self.over_count == 2:
                self.game_over = True
                self.winner = "Петя"
                return "перебор (второй) - Петя победил"
            else:
                return "перебор"

class PetiaComputer(Petia):
    def __init__(self):
        self.secret = random.randint(1, 2012)
        self.over_count = 0
        self.game_over = False
        self.winner = None

    def check(self, guess):
        if guess == self.secret:
            self.game_over = True
            self.winner = "Коля"
            return "угадал"
        elif guess < self.secret:
            return "недобор"
        else:
            self.over_count += 1
            if self.over_count == 2:
                self.game_over = True
                self.winner = "Петя"
                return "перебор (второй) - Петя победил"
            else:
                return "перебор"

class Kolya:
    pass

class KolyaHuman(Kolya):
    def guess(self):
        while True:
            try:
                value = int(input("Игрок Коля, назовите натуральное число от 1 до 2012: "))
                if 1 <= value <= 2012:
                    return value
                else:
                    print("Число должно быть от 1 до 2012.")
            except ValueError:
                print("Пожалуйста, введите целое число.")

class Game:
    def __init__(self, mode):
        self.mode = mode
        if mode == "1":
            self.petia = PetiaHuman()
            self.kolya = KolyaHuman()
            self.mode_name = "Игрок против игрока (Петя и Коля за одним компьютером)"
        else:
            self.petia = PetiaComputer()
            self.kolya = KolyaHuman()
            self.mode_name = "Игрок против компьютера (Вы - Коля, компьютер - Петя)"

    def play(self):
        print(f"Режим: {self.mode_name}")
        if self.mode == "2":
            print("Компьютер (Петя) загадал число от 1 до 2012.")
        while not self.petia.game_over:
            guess = self.kolya.guess()
            result = self.petia.check(guess)
            print(result)
            if result == "угадал":
                break
        print(f"Победитель: {self.petia.winner}")

if __name__ == "__main__":
    print("Выберите режим:")
    print("1 - Игрок против игрока (Петя загадывает, Коля отгадывает)")
    print("2 - Игрок против компьютера (Вы - Коля, компьютер - Петя)")
    mode = input("Ваш выбор (1 или 2): ").strip()
    while mode not in ("1", "2"):
        mode = input("Неверный ввод. Выберите 1 или 2: ").strip()
    game = Game(mode)
    game.play()