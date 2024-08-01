import pandas as pd
from util import ChessBoard

if __name__ == "__main__":
    # train FEN
    train_fen = pd.read_csv("train_fen.csv")
    train_fen_list = list(train_fen["FEN"])

    # train data
    df = pd.DataFrame(columns=["Question", "Context", "Answer"])

    for fen in train_fen_list:
        chessboard = ChessBoard(fen)
        analysis = chessboard.parse_fen_cot()
        question, piece, gt = chessboard.get_question_gt(analysis)
        data = {"Question": question,
                "Context": "",
                "Answer": analysis + chessboard.generate_answer_summary(piece, gt)}
        df.loc[df.shape[0]] = data

    df.to_csv("final_train_fen.csv", index=False)
    print("[INFO] CSV generated")
        # print(question)
        # print("="*20)
        # print(gt)
        # print("="*20)
        # print(analysis)
        # print(chessboard.generate_answer_summary(piece, gt))
