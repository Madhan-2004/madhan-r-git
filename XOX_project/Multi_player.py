from XOX_project.Base_page import TicTacToe, initial_board


class MultiPlayer(TicTacToe):
    def play(self):
        print("Let's play Tic Tac Toe\nThis is the position...")
        initial_board()
        print("\nand -1 for surrender...\nShall we start! who's gonna play first...")
        while True:
            start = input("X or O: ").upper()
            if start in ["X", "O"]:
                break
            else:
                print('***ENTER PROPER INPUT***')
        player1_symbol = start
        player2_symbol = "O" if player1_symbol == "X" else "X"

        for _ in range(4):
            self.player_move(player1_symbol)
            self.player_move(player2_symbol)
        self.player_move(player1_symbol)
        print("CONGRATS GUYS ITS A DRAW")
