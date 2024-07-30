
from util import ChessBoard

if __name__ == "__main__":
    FEN = "4r1k1/1pR3p1/p2pn1qp/8/PPBP4/1QP1n3/3N2PP/5RK1 w - - 1 26"
    chessboard = ChessBoard(FEN)
    print(chessboard.parse_fen_cot())
