import random

class Player:
    def __init__(self, name, is_human):
        self.name = name
        self.is_human = is_human

    def choose_card_phase1(self, available):
        if self.is_human:
            print(f"{self.name}, доступные карточки: {available}")
            while True:
                try:
                    val = int(input("Выберите число от 1 до 8: "))
                    if val in available and available[val] > 0:
                        return val
                    else:
                        print("Неверный выбор, попробуйте снова.")
                except ValueError:
                    print("Введите число.")
        else:
            candidates = [v for v, cnt in available.items() if cnt > 0]
            return random.choice(candidates)

    def choose_card_phase2(self, deck):
        if self.is_human:
            print(f"{self.name}, колода: {deck}")
            while True:
                try:
                    idx = int(input(f"Выберите индекс карточки (0-{len(deck)-1}): "))
                    if 0 <= idx < len(deck):
                        return deck[idx]
                    else:
                        print("Неверный индекс.")
                except ValueError:
                    print("Введите число.")
        else:
            return random.choice(deck)

    def decide_stop(self):
        if self.is_human:
            answer = input("Петя, сказать 'стоп'? (y/n): ").strip().lower()
            return answer == 'y'
        else:
            return random.choice([True, False])

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.initial_cards = {i: i for i in range(1, 9)}
        self.drawn_cards = []
        self.sequence = []
        self.current_player = 0
        self.phase = 1
        self.stop_called = False

    def all_cards_taken(self):
        return sum(self.initial_cards.values()) == 0

    def start_phase2(self):
        self.phase = 2
        self.current_player = 1
        self.sequence.clear()
        print("\n--- Второй этап: выкладывание карточек ---")
        print(f"Колода: {self.drawn_cards}")

    def is_difference_of_squares(self, n):
        return n % 4 != 2

    def play_phase1_turn(self):
        player = self.players[self.current_player]
        val = player.choose_card_phase1(self.initial_cards)
        self.initial_cards[val] -= 1
        self.drawn_cards.append(val)
        print(f"{player.name} взял карточку {val}. Колода: {self.drawn_cards}")

        if self.all_cards_taken():
            print("Все карточки разобраны. Переход ко второму этапу.")
            self.start_phase2()
            return

        if self.current_player == 1:
            print("Ход Васи завершён.")
            if self.players[0].decide_stop():
                print("Петя сказал 'стоп'! Невыбранные карточки убираются.")
                self.start_phase2()
                return

        self.current_player = 1 - self.current_player

    def play_phase2_turn(self):
        player = self.players[self.current_player]
        if not self.drawn_cards:
            return
        chosen = player.choose_card_phase2(self.drawn_cards)
        self.drawn_cards.remove(chosen)
        self.sequence.append(chosen)
        print(f"{player.name} выложил карточку {chosen}. Последовательность: {self.sequence}")
        self.current_player = 1 - self.current_player

    def determine_winner(self):
        number = int(''.join(str(d) for d in self.sequence))
        print(f"\nПолученное число: {number}")
        if self.is_difference_of_squares(number):
            print("Вася (игрок 2) победил!")
        else:
            print("Петя (игрок 1) победил!")

    def run(self):
        print("=== Игра 'Разность квадратов' ===")
        while self.phase == 1:
            self.play_phase1_turn()
            if self.phase == 2:
                break

        while self.phase == 2 and self.drawn_cards:
            self.play_phase2_turn()

        self.determine_winner()

def main():
    print("Выберите режим игры:")
    print("1. Человек против компьютера")
    print("2. Человек против человека")
    mode = input("Ваш выбор (1/2): ").strip()

    if mode == '1':
        print("Кто будет Петей (первый игрок)?")
        print("1. Человек")
        print("2. Компьютер")
        first = input("Выбор (1/2): ").strip()
        if first == '1':
            player1 = Player("Петя (человек)", True)
            player2 = Player("Вася (компьютер)", False)
        else:
            player1 = Player("Петя (компьютер)", False)
            player2 = Player("Вася (человек)", True)
        game = Game(player1, player2)
    else:
        player1 = Player("Петя (человек)", True)
        player2 = Player("Вася (человек)", True)
        game = Game(player1, player2)

    game.run()

if __name__ == "__main__":
    main()