
from util import ChessBoard

if __name__ == "__main__":
    FEN = "4r1k1/1pR3p1/p2pn1qp/8/PPBP4/1QP1n3/3N2PP/5RK1 w - - 1 26"
    chessboard = ChessBoard(FEN)
    analysis = chessboard.parse_fen_cot()
    question, piece, gt = chessboard.get_question_gt(analysis)
    print(question)
    print("="*20)
    print(gt)
    print("="*20)
    print(analysis)
    print(chessboard.generate_answer_summary(piece, gt))
