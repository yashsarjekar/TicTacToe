from .player import Player
from .piece_x import PieceX
from .piece_o import PieceO
from .board import Board

class Game:

    def __init__(self, size):
        self.size = size
        self.players = []
        self.board = None

    def initialize_game(self, size, no_players):
        """Initialize Tic Tac Toe Game.

        Args:
            size (int): size of board
            no_players (int): Number of players.
        """
        #Two players for now
        x_piece = PieceX()
        player_1 = Player(1, "Player 1", x_piece.piece_type)
        o_piece = PieceO()
        player_2 = Player(2, "Player 2", o_piece.piece_type)
        self.board = Board(size)

        self.players.append(player_1)
        self.players.append(player_2)

    def start_game(self):
        """Start Game functionality.
        """

        winners_flag = False
        tie = False
        while winners_flag == False:
            player = self.players.pop(0)
            print(f"[INFO] Player {player.player_name} is playing the move")
            free_space = self.board.get_free_space()
            if len(free_space) == 0 and winners_flag == False:
                tie = True
                break
            print('[INFO] Board before adding for piece')
            self.board.print_board()
            row = int(input("Enter the row you want to add piece: "))
            col = int(input("Enter the col you want to add piece: "))

            if 0 <= row < self.size and 0 <= col < self.size:
                add_piece = self.board.add_piece(row, col, player.piece)

                if add_piece == False:
                    self.players.insert(0, player)
                    print('[INFO] Player has added piece to Invalid Position. Try again!')
                    continue
                print('[INFO] Board after adding for piece')
                self.board.print_board()  
                res = self.winner_checker(row, col, player.piece)
                if res:
                    winners_flag = True
                    print(f'[INFO] {player.player_name} with piece {player.piece} has Won')
                    break
                self.players.append(player)
            else:
                self.players.insert(0, player)
                print("[INFO] Invalid Position. Try again")
                continue
            print('**************************************************************************')

        if tie:
            print('[INFO] Game is a Tie!')

    def winner_checker(self, row_no, col_no, piece):
        """Check winner if found or not.

        Args:
            row_no (int): row number of board
            col_no (int): col number of board
            piece (str): piece symbol

        Returns:
            boolean: Winner found True and for not found False.
        """
        rowcheck = True
        colcheck = True
        diagonalcheck = True
        antidaiagonalcheck = True

        #row check
        for col in range(self.size):
            if self.board.board[row_no][col] == (row_no, col) or self.board.board[row_no][col] != piece:
                rowcheck = False
                break

        #col check
        for row in range(self.size):

            if self.board.board[row][col_no] == (row, col_no) or self.board.board[row][col_no] != piece:
                colcheck = False
                break

        #diagonal
        for ind in range(self.size):

            if self.board.board[ind][ind] == (ind, ind) or self.board.board[ind][ind] != piece:
                diagonalcheck = False
                break
        
        #antidiagonal
        for ind in range(self.size):

            if self.board.board[ind][self.size - ind - 1] == (ind, ind) or self.board.board[ind][self.size - ind - 1] != piece:
                antidaiagonalcheck = False
                break

        if rowcheck or colcheck or diagonalcheck or antidaiagonalcheck:
            return True
        
        return False