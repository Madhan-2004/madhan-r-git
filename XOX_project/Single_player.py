import random as rn
import time as tm

from XOX_project.Base_page import TicTacToe, initial_board


class SinglePlayer(TicTacToe):
    def __init__(self, difficulty):
        super().__init__()
        self.difficulty = difficulty

    def easy_move(self, symbol):
        tm.sleep(1.1)
        move = rn.choice(list(self.available_positions))
        self.available_positions.remove(move)
        self.repeated_positions.add(move)
        self.board[move - 1] = symbol
        self.print_board()
        if self.is_winner(symbol):
            print("\n***PC WON***")
            exit()

    def hard_move(self, symbol):
        tm.sleep(0.8)
        move = self.calculate_best_move(symbol)
        self.available_positions.remove(move)
        self.repeated_positions.add(move)
        self.board[move - 1] = symbol
        self.print_board()
        if self.is_winner(symbol):
            print("\n***PC WON***")
            exit()

    def calculate_best_move(self, symbol):
        opponent_symbol = 'O' if symbol == 'X' else 'X'

        # Check if we can win in the next move
        for pos in self.available_positions:
            self.board[pos - 1] = symbol
            if self.is_winner(symbol):
                self.board[pos - 1] = " "
                return pos
            self.board[pos - 1] = " "

        # Check if the opponent can win in their next move, and block them
        for pos in self.available_positions:
            self.board[pos - 1] = opponent_symbol
            if self.is_winner(opponent_symbol):
                self.board[pos - 1] = " "
                return pos
            self.board[pos - 1] = " "

        # Try to take the center
        if 5 in self.available_positions:
            return 5

        # Try to take one of the corners
        for pos in [1, 3, 7, 9]:
            if pos in self.available_positions:
                return pos

        # Take any available position (shouldn't reach this in a properly played game)
        return rn.choice(list(self.available_positions))

    def play(self):
        print("Let's play Tic Tac Toe\nThis is the position...")
        initial_board()
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
