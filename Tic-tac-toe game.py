import random
import time

# Ігрове поле (9 порожніх клітинок)
board = [' '] * 9


def show_board():
    print("\n")
    # Відображаємо ігрове поле та номери позицій для зручності
    print(f" {board[0]} | {board[1]} | {board[2]}    1 | 2 | 3")
    print("-----------    -----------")
    print(f" {board[3]} | {board[4]} | {board[5]}    4 | 5 | 6")
    print("-----------    -----------")
    print(f" {board[6]} | {board[7]} | {board[8]}    7 | 8 | 9")
    print("\n")


def check_win(mark):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонталі
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикалі
        (0, 4, 8), (2, 4, 6)  # Діагоналі
    ]
    # Перевіряємо, чи є хоча б одна виграшна лінія
    return any(board[a] == board[b] == board[c] == mark for a, b, c in wins)


def get_ai_move(mode):
    # Легкий режим: просто випадковий хід
    if mode == 'easy':
        available = [i for i in range(9) if board[i] == ' ']
        return random.choice(available)

    # Важкий режим (Hard)
    # 1. Спробувати перемогти зараз
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win('O'):
                board[i] = ' '  # Повертаємо назад
                return i
            board[i] = ' '

    # 2. Заблокувати гравця (якщо він може виграти наступним ходом)
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win('X'):
                board[i] = ' '
                return i
            board[i] = ' '

    # 3. Зайняти центр
    if board[4] == ' ':
        return 4

    # 4. Зайняти кути
    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] == ' ']
    if available_corners:
        return random.choice(available_corners)

    # 5. Будь-яка вільна клітинка
    available = [i for i in range(9) if board[i] == ' ']
    return random.choice(available)


def play_game():
    global board
    board = [' '] * 9  # Очищуємо поле перед грою

    print("Welcome to Tic Tac Toe!")
    print("Select mode:")
    print("1. Player vs Player")
    print("2. Player vs Computer (easy)")
    print("3. Player vs Computer (hard)")

    choice = input("Enter choice (1-3): ")
    ai_mode = 'easy' if choice == '2' else 'hard' if choice == '3' else None

    for turn in range(9):
        show_board()
        current_player = 'X' if turn % 2 == 0 else 'O'

        if current_player == 'O' and ai_mode:
            print(f"Computer ({ai_mode}) is thinking...")
            time.sleep(1)
            pos = get_ai_move(ai_mode)
        else:
            # Хід людини
            while True:
                try:
                    move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
                    if 0 <= move <= 8 and board[move] == ' ':
                        pos = move
                        break
                    else:
                        print("Invalid position or already taken. Try again.")
                except ValueError:
                    print("Please enter a number between 1 and 9.")

        board[pos] = current_player

        if check_win(current_player):
            show_board()
            if current_player == 'O' and ai_mode:
                print("Computer wins!")
            else:
                print(f"Player {current_player} wins!")
            return

    show_board()
    print("It's a draw!")


# Запуск гри
if __name__ == "__main__":
    play_game()
