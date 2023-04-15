from .piece_type import PieceType
from .piece_symbol import PieceSymbol

class PieceO(PieceType):

    def __init__(self):
        super().__init__(PieceSymbol.o_symbol)