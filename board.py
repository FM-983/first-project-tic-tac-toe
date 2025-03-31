
class Board:
    def __init__(self):
        self.board = [" "] * 9

    def display(self):
        print("POSITIONS =\n        1 || 2 || 3\n        4 || 5 || 6\n        7 || 8 || 9")
        print("  ******|||Board|||******")
        print("*--------" * 3, "*", sep="")
        for i in range(9):
            print("|  ", self.board[i], end="   |")
            if (i + 1) % 3 == 0:
                print("\n" + "+--------" * 3 + "+")

    def place_token(self, position, token):
         self.board[position] = token

    def is_valid_move(self, position):
        return 0 <= position < 9 and self.board[position] == " "

    def check_winner(self, token):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]
        return any(all(self.board[i] == token for i in combo) for combo in win_combinations)

    def is_full(self):
        return all(cell in ["x", "o"] for cell in self.board)
