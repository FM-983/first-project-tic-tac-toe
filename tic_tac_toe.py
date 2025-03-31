import random
from player import Player
from game import Game
from board import Board

class TicTacToe:
    def __init__(self):
        pass

    def choose_token(self, player1_name):
        while True:
            choice = input(f"{player1_name}, choose a token (x/o) or press Enter for random: ").lower()
            if choice in ["x", "o"]:
                return ["x", "o"] if choice == "x" else ["o", "x"]
            elif choice == "":
                tokens = ["x", "o"]
                random.shuffle(tokens)
                print(f"{player1_name} will be '{tokens[0]}'")
                return tokens
            else:
                print("Invalid choice. Try again.")

    def play_vs_player(self):
        name1 = input("Insert first player name: ").strip()
        name2 = input("Insert second player name: ").strip()
        tokens = self.choose_token(name1)
        player1 = Player(name1, tokens[0])
        player2 = Player(name2, tokens[1])
        game = Game(player1, player2, Board())
        game.play()

    def play_vs_computer(self):
        name1 = input("Insert your name: ").strip()
        tokens = self.choose_token(name1)
        player1 = Player(name1, tokens[0])
        computer = Player("Computer", tokens[1])
        game = Game(player1, computer, Board())
        game.play()

    def menu(self):
        while True:
            print("\n***** WELCOME TO TIC-TAC-TOE *****")
            print("1. Play against another player")
            print("2. Play against the computer")
            print("3. Quit")
            option = input("Choose an option (1/2/3): ").strip()
            if option == "1":
                self.play_vs_player()
            elif option == "2":
                self.play_vs_computer()
            elif option == "3":
                print("Thank you for playing!")
                break
            else:
                print("Invalid option. Try again.")
