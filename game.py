import random

class Game:
    def __init__(self, player1, player2, board):
        self.players = [player1, player2]
        self.board = board
        self.current = 0  # index of current player

    def switch_turn(self):
        self.current = 1 - self.current

    def get_current_player(self):
        return self.players[self.current]

    def play(self):
        while True:
            self.board.display()
            player = self.get_current_player()
            print(f"{player.name}'s turn with token ({player.token})")

            if player.name == "Computer":
                position = random.choice([i for i in range(9) if self.board.is_valid_move(i)])
            else:
                while True:
                    try:
                        position = int(input("Enter position (1-9): ")) - 1
                        if self.board.is_valid_move(position):
                            break
                        else:
                            print("Invalid move. Try again.")
                    except ValueError:
                        print("Please enter a valid number.")

            self.board.place_token(position, player.token)

            if self.board.check_winner(player.token):
                self.board.display()
                print(f"Congratulations {player.name}, you win!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break

            self.switch_turn()