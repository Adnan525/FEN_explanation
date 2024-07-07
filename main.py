def fen_to_board(fen: str) -> str:
    """
    Converts a FEN string into a board state
    :param fen: fen string, e.g. 2r3k1/p4p1p/4pp2/1b6/pP1P3P/P3PN2/2rN1PP1/R3K2R w KQ - 1 20
    :return: the board state, with empty square denoted as 1
    """
    rows = fen.split(' ')[0].split('/')
    board = ""
    for row in rows:
        board_row = ""
        for char in row:
            if char.isdigit():
                board_row += " 1" * int(char)
            else:
                board_row += " " + char
        board += board_row + "\n"
    return board


FEN = "1R6/p3k1p1/2p2b2/2Pn4/1BQPB3/P7/6PP/3q2K1 w - - 1 33"
result = fen_to_board(FEN)
print(result)

