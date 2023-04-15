from .piece_type import PieceType
from .piece_symbol import PieceSymbol

class PieceX(PieceType):

    def __init__(self):
        super().__init__(PieceSymbol.x_symbol)