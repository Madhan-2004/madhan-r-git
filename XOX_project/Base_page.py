def initial_board():
    print(f"\n 1 | 2 | 3 "
          f"\n-----------\n 4 | 5 | 6 "
          f"\n-----------\n 7 | 8 | 9 ")


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.positions = list(range(1, 10))
        self.available_positions = set(range(1, 10))
        self.repeated_positions = set()

    def print_board(self):
        print(f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} "
              f"\n-----------\n {self.board[3]} | {self.board[4]} | {self.board[5]} "
              f"\n-----------\n {self.board[6]} | {self.board[7]} | {self.board[8]}")

    def is_winner(self, symbol):
        b = self.board
        return (b[0] == b[1] == b[2] == symbol) or (b[3] == b[4] == b[5] == symbol) or \
               (b[6] == b[7] == b[8] == symbol) or (b[0] == b[3] == b[6] == symbol) or \
               (b[1] == b[4] == b[7] == symbol) or (b[2] == b[5] == b[8] == symbol) or \
               (b[0] == b[4] == b[8] == symbol) or (b[2] == b[4] == b[6] == symbol)

    def player_move(self, symbol):
        print(f"\n{symbol}'s turn...")
        while True:
            try:
                position = int(input("Enter position: "))
                if position == -1:
                    p2 = 'X' if symbol == "O" else "O"
                    print(f"\n{symbol} surrenders\n{p2} WON!")
                    exit()
                if position in self.available_positions:
                    self.available_positions.remove(position)
                    self.repeated_positions.add(position)
                    self.board[position - 1] = symbol
                    self.print_board()
                    if self.is_winner(symbol):
                        print(f"\n*** {symbol} WON ***")
                        exit()
                    break
                else:
                    print(f"***Invalid input***\nChoose from these {self.available_positions}\n")
            except ValueError:
                print(f"***Invalid input***\nChoose from these {self.available_positions}\n")
