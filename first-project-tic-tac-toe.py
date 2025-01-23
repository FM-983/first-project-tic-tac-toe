import random

def print_board(board):
    print("POSITIONS =\n        1 || 2 || 3\n        4 || 5 || 6\n        7 || 8 || 9")
    print("  ******|||Board|||******")
    print("*--------" * 3, "*", sep="")
    for i, position in enumerate(board):
        print("|  ", board[i], end="   |")
        if (i + 1) % 3 == 0:
            print("")
            print("+--------" * 3, "+", sep="")


def players():
    while True:
        player1 = input("Insert the First player name: ")
        if not player1:
            print("Player name cannot be empty. Please enter a valid name.")
            continue
        player2 = input("Insert the Second player name: ")
        if not player2:
            print("Player name cannot be empty. Please enter a valid name.")
            continue
        return player1, player2


def choose_token(player1):
    while True:
        try:
            token_choose = input(
                f"{player1}, choose a token to play (x, o, or press 'Enter' for random choice): "
            ).lower()
            if token_choose == "x":
                return ["x", "o"]
            elif token_choose == "o":
                return ["o", "x"]
            elif not token_choose:
                tokens = ["x", "o"]
                random.shuffle(tokens)
                print(f"{player1} will play with {tokens[0]}")
                return tokens
            else:
                print("Invalid token choice. Please choose 'x' or 'o'.")
        except ValueError:
            print("Invalid input. Please enter (x/o).")


def player_choice(board):
    while True:
        try:
            position = int(input("Enter the position (1-9): "))
            if 1 <= position <= 9 and board[position - 1] not in ["x", "o"]:
                return position - 1
            else:
                print("Invalid position. Please choose an empty position.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def place_token(board, position, token):
    board[position] = token


def check_winner(board, token):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]
    for combination in win_combinations:
        if all(board[i] == token for i in combination):
            return True
    return False


def play_2v2():
    board = [" "] * 9
    player1, player2 = players()
    tokens = choose_token(player1)
    current_player = player1
    current_token = tokens[0]
    tokens_in_board = 0

    while True:
        print_board(board)
        print(f"{current_player}'s Turn, with the token: ({current_token})")
        position = player_choice(board)
        place_token(board, position, current_token)

        tokens_in_board += 1

        if check_winner(board, current_token):
            print_board(board)
            print(f"Congratulations {current_player}! You win!")
            break

        if tokens_in_board == 9:
            print_board(board)
            print("It's a tie!")
            break

        if current_player == player1:
            current_player = player2
            current_token = tokens[1]
        else:
            current_player = player1
            current_token = tokens[0]
    while True:
        try:
            restart = input("Do you want to play again 2v2? (yes/no): ").lower()
            if restart == "yes":
                play_2v2()
                break
            elif restart == "no":
                print("*****MENU*****")
                break
            else:
                print("Invalid input. Please enter 'yes', 'no': ")
        except Exception as e:
            print(f"An error occurred: {e}")





def name_1_vs_pc():
    while True:
        player1 = input("Insert the First player name: ")
        if not player1:
            print("Player name cannot be empty. Please enter a valid name.")
            continue
        else:
            return player1

def play_against_computer():
    board = [" "] * 9
    player1 = name_1_vs_pc()
    tokens = choose_token(player1)
    computer_token = tokens[1]
    current_player = player1
    current_token = tokens[0]
    tokens_in_board = 0

    while True:
        print_board(board)
        if current_player == player1:
            print(f"{current_player}'s Turn, with the token: ({current_token})")
            position = player_choice(board)
        else:
            print("Computer's Turn...")
            position = random.choice([i for i in range(9) if board[i] == " "])

        place_token(board, position, current_token)

        tokens_in_board += 1

        if check_winner(board, current_token):
            print_board(board)
            if current_player == player1:
                print(f"Congratulations {player1}! You win!")
            else:
                print("Computer wins! Better luck next time!")
            break

        if tokens_in_board == 9:
            print_board(board)
            print("It's a tie!")
            break

        if current_player == player1:
            current_player = "Computer"
            current_token = computer_token
        else:
            current_player = player1
            current_token = tokens[0]

    while True:
        try:
            restart = input("Do you want to play again PC ? (yes/no): ").lower()
            if restart == "yes":
                play_against_computer()
                break
            elif restart == "no":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please enter 'yes', 'no': ")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    while True:
        try:
            mode = input("Do you want to play against another player or the computer? (player/computer) 'q' to end the program: ").lower()

            if mode == "player":
                play_2v2()
            elif mode == "computer":
                play_against_computer()
            elif mode == "q":
                print("Thank you for playing Tic-Tac-Toe! Goodbye!")
                return True
        except ValueError:
            print("Invalid input.")


main()
