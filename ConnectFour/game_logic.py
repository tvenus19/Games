import numpy as np

class Game:
    def __init__(self, row_count, column_count):
        self.row_count = row_count
        self.column_count = column_count
        self.board = self.create_board()
        self.game_over = False
        self.turn = 0

    def create_board(self):
        return np.zeros((self.row_count,self.column_count))

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[self.row_count-1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.row_count):
            if self.board[r][col] == 0:
                return r

    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(self.column_count - 3):
            for r in range(self.row_count):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.column_count):
            for r in range(self.row_count - 3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(self.column_count - 3):
            for r in range(self.row_count - 3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.column_count - 3):
            for r in range(3, self.row_count):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

    def is_tie(self):
        return np.all(self.board)

    def print_board(self):
        print(np.flip(self.board, 0))
