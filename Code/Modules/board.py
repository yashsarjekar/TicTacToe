class Board:

    def __init__(self, size):
        self.size = size
        self.board = [[(row, col) for col in range(self.size)] for row in range(self.size)]

    def get_free_space(self):
        """Finds free spaces on board

        Returns:
            list: list of free spaces.
        """
        free_space = []

        for row in range(self.size):

            for col in range(self.size):

                if self.board[row][col] == (row, col):

                    free_space.append([row, col])

        return free_space

    def print_board(self):
        """Print Board
        """
        for row in range(self.size):

            for col in range(self.size):
                if col == self.size - 1:
                    print(self.board[row][col])
                else:
                    print(self.board[row][col], '|', end= '')

    def add_piece(self, row, col, piece_symbol):
        """Adding piece to board

        Args:
            row (int): row number of board
            col (int): col number of board
            piece_symbol (str): symbol of piece

        Returns:
            boolean: Piece added on board or not
        """
        if self.board[row][col] == (row, col):
            # free space
            self.board[row][col] = piece_symbol
            return True
        else:
            return False
