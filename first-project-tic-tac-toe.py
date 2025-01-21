import random


def print_board(board):
    print("POSITIONS =\n        1 || 2 || 3\n        4 || 5 || 6\n        7 || 8 || 9")
    print("  ******|||Board|||******")
    print("*--------" * 3, "*", sep="")
    for i , position in enumerate(board):
        print("|  " ,board[i], end="   |")
        if (i+1) % 3 == 0:
            print("")
            print("+--------" * 3,"+",sep="")


def players():
    print("Welcome to Tic-Tac-Toe!")

    player1 = input("Insert the First player name: ")
    player2 = input("Insert the Second player name: ")
    while True:
        try:
            token_choose = input(
                f"{player1}, choose a token to play (x, o, or press 'Enter' for random choice): "
            ).lower()
            if token_choose == "x":
                tokens = ["x", "o"]
            elif token_choose == "o":
                tokens = ["o", "x"]
            elif not token_choose:
                possible_tokens = ["x", "o"]
                random.shuffle(possible_tokens)
                tokens = possible_tokens
                print(f"{player1} will play with {tokens[0]}")
            else:
                print("Invalid token choice. Please choose 'x' or 'o'.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter 'x' or 'o'.")
            continue

        return player1, player2, tokens


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
        [0, 1, 2],[3, 4, 5],[6, 7, 8],
        [0, 3, 6],[1, 4, 7],[2, 5, 8],
        [0, 4, 8],[2, 4, 6],
    ]
    for combination in win_combinations:
        if all(board[i] == token for i in combination):
            return True
    return False


def play_game():

    board = [" "] * 9
    player1, player2, tokens = players()
    current_player = player1
    current_token = tokens[0]
    tokens_in_board = 0
    turn = True

    while turn:

        print_board(board)
        print(f"{current_player}'s Turn ,with the token: ({current_token})")
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

    restart = input("Do you want to play again? (yes/no): ").lower()
    if restart == "yes":
        play_game()
    else:print("Thank you for playing Tic-Tac-Toe! Goodbye!")
    return



play_game()
