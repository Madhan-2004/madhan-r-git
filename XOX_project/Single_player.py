from XOX import TicTacToe
import random as rn
import time as tm


class SinglePlayer(TicTacToe):
    def __init__(self, difficulty):
        super().__init__()
        self.difficulty = difficulty

    def easy_move(self, symbol):
        tm.sleep(1.2)
        move = rn.choice(list(self.available_positions))
        self.available_positions.remove(move)
        self.repeated_positions.add(move)
        self.board[move - 1] = symbol
        self.print_board()
        if self.is_winner(symbol):
            print("\n***PC WON***")
            exit()

    def hard_move(self, symbol):
        tm.sleep(1.2)
        move = self.calculate_best_move(symbol)
        self.available_positions.remove(move)
        self.repeated_positions.add(move)
        self.board[move - 1] = symbol
        self.print_board()
        if self.is_winner(symbol):
            print("\n***PC WON***")
            exit()

    def calculate_best_move(self, symbol):
        for pos in self.available_positions:
            self.board[pos - 1] = symbol
            if self.is_winner(symbol):
                self.board[pos - 1] = " "
                return pos
            self.board[pos - 1] = " "
        return rn.choice(list(self.available_positions))

    def play(self):
        print("Let's play Tic Tac Toe\nThis is the position...")
        self.initial_board()
        print("\nand -1 for surrender...\nSo Choose your side...")
        start = input("X or O: ").upper()
        while start not in ["X", "O"]:
            print('***ENTER PROPER INPUT***')
            start = input("X or O: ").upper()
        player_symbol = start
        pc_symbol = "O" if player_symbol == "X" else "X"

        for _ in range(4):
            self.player_move(player_symbol)
            if self.difficulty == "E":
                self.easy_move(pc_symbol)
            else:
                self.hard_move(pc_symbol)
        self.player_move(player_symbol)
        print("CONGRATS ITS A DRAW")
