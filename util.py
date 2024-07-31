import random
import re


def count_characters(input_string):
    character_count = {}
    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


class ChessBoard:
    def __init__(self, fen: str):
        self.fen = fen
        self.board = self.fen_to_board()
        self.piece_positions = self.get_piece_positions()
        random.seed(42)

    def fen_to_board(self) -> str:
        """
        Converts a FEN string into a board state
        :param: fen string, e.g. 2r3k1/p4p1p/4pp2/1b6/pP1P3P/P3PN2/2rN1PP1/R3K2R w KQ - 1 20
        :return: the board state, with empty square denoted as 1
        """
        rows = self.fen.split(" ")[0].split("/")
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

    def count_pieces(self) -> str:
        """
        Counts the number of pieces in a FEN string
        :param: the original FEN string
        :return: number of chess pieces present in the game
        """
        white_piece_pattern = r"[A-Z]"
        black_piece_pattern = r"[a-z]"
        piece_dictionary = {"P": "White Pawn", "N": "White Knight",
                            "B": "White Bishop", "R": "White Rook",
                            "Q": "White Queen", "K": "White King",
                            "p": "Black Pawn", "n": "Black Knight",
                            "b": "Black Bishop", "r": "Black Rook",
                            "q": "Black Queen", "k": "Black King"}

        fen_pieces = self.fen.split(" ")[0]

        white_pieces_count = len(re.findall(white_piece_pattern, fen_pieces))
        white_pieces = count_characters(re.findall(white_piece_pattern, fen_pieces))
        black_pieces_count = len(re.findall(black_piece_pattern, fen_pieces))
        black_pieces = count_characters(re.findall(black_piece_pattern, fen_pieces))
        return f"   - Total {white_pieces_count + black_pieces_count} pieces present in the board\n   - White Pieces: {white_pieces_count} pieces which are {', '.join([f'{white_pieces[p]} x {piece_dictionary[p]}' for p in white_pieces.keys()])}\n   - Black Pieces: {black_pieces_count} pieces which are {', '.join([f'{black_pieces[p]} x {piece_dictionary[p]}' for p in black_pieces])}\n"

    def get_piece_positions(self) -> dict[str, str]:
        """
        Gets the positions of all pieces in Algebraic Notation
        :param: output of fen_to_board
        :return: Algebraic Notation for each piece present in a dictionary
        """
        position = {}
        rank_dictionary = {0: "a", 2: "b", 4: "c", 6: "d", 8: "e", 10: "f", 12: "g", 14: "h"}
        file_dictionary = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
        piece_dictionary = {"P": "White Pawn", "N": "White Knight",
                            "B": "White Bishop", "R": "White Rook",
                            "Q": "White Queen", "K": "White King",
                            "p": "Black Pawn", "n": "Black Knight",
                            "b": "Black Bishop", "r": "Black Rook",
                            "q": "Black Queen", "k": "Black King"}
        pattern_to_detect_pieces = r"[a-zA-Z]"
        board_state = self.board.split("\n")[:-1]

        for file, row in enumerate(board_state):
            row = row.strip()
            for rank, piece in enumerate(row):
                if re.fullmatch(pattern_to_detect_pieces, piece):
                    prev_string = position[piece_dictionary[piece]] if position.get(piece_dictionary[piece]) else ""
                    position[piece_dictionary[
                        piece]] = f"{prev_string} {rank_dictionary[rank]}{file_dictionary[file]}".strip()

        return position

    def get_piece_placement_text(self) -> str:
        """
        :param: pass the FULL FEN
        :return: returns a formatted string
        """
        target = self.fen.split(" ")[0]
        return f"Piece Placement:\n   - {target}\n   - This represents the board from the 8th rank to the 1st rank.\n   - Each rank is separated by a '/'.\n   - Numbers represent empty squares, and letters represent pieces (uppercase for White, lowercase for Black)\n"

    def get_active_colour(self) -> str:
        """
        returns the active player
        :param: Full FEN
        :return: processed string
        """
        target = self.fen.split(" ")[1]
        return f"Active Colour:\n   - {target} indicates it is {'White' if target == 'w' else 'Black'}'s turn to move.\n"

    def get_castling_availability(self) -> str:
        """
        Returns the castling availability
        :param: Full FEN
        :return: processed string
        """
        target = self.fen.split(" ")[2]
        if target == "-":
            return "Castling Availability:\n   - Neither side can castle.\n"

        castling = []
        if "K" in target:
            castling.append("White can castle kingside")
        if "Q" in target:
            castling.append("White can castle queenside")
        if "k" in target:
            castling.append("Black can castle kingside")
        if "q" in target:
            castling.append("Black can castle queenside")

        return f"Castling Availability:\n   - {', '.join(castling)}." + "\n"

    def get_en_passant_target(self) -> str:
        """
        Returns the en passant target square
        :param: Full FEN
        :return: processed string
        """
        target = self.fen.split(" ")[3]
        if target == "-":
            return "En Passant Target Square:\n   - There is no en passant target square.\n"
        return f"En Passant Target Square:\n   - The en passant target square is {target}.\n"

    def get_halfmove_clock(self) -> str:
        """
        Returns the halfmove clock value
        :param: Full FEN
        :return: processed string
        """
        target = self.fen.split(" ")[4]
        return f"Halfmove Clock:\n   - The halfmove clock is {target}. This is the number of halfmoves since the last pawn advance or capture."

    def get_fullmove_number(self) -> str:
        """
        Returns the fullmove number
        :param: Full FEN
        :return: processed string
        """
        target = self.fen.split(" ")[5]
        return f"Fullmove Number:\n   - The fullmove number is {target}. This indicates that this is the {target}th full move in the game.\n\n"

    def explain_board_state(self) -> str:
        """
        Provides a comprehensive explanation of the board state given a FEN string
        :param: Full FEN string
        :return: Detailed explanation of the board state
        """
        explanation = "Detailed Board State:\n"

        ranks = self.fen.split()[0].split('/')
        for i, rank in enumerate(ranks):
            rank_number = 8 - i
            explanation += f"- {rank_number}th Rank: {rank}\n"
            explanation += "  - "
            square = 0
            for char in rank:
                if char.isdigit():
                    empty_squares = int(char)
                    if empty_squares == 1:
                        explanation += "One empty square, "
                    else:
                        explanation += f"{empty_squares} empty squares, "
                    square += empty_squares
                else:
                    piece_name = {"K": "King", "Q": "Queen", "R": "Rook", "B": "Bishop", "N": "Knight", "P": "Pawn",
                                  "k": "King", "q": "Queen", "r": "Rook", "b": "Bishop", "n": "Knight", "p": "Pawn"}
                    color = "White" if char.isupper() else "Black"
                    file = chr(ord('a') + square)
                    explanation += f"{color} {piece_name[char]} on {file}{rank_number}, "
                    square += 1
            explanation = explanation.rstrip(', ') + "\n\n"

        return explanation

    def parse_fen_cot(self) -> str:
        parse = ""
        default_string = '''A FEN string is divided into six fields separated by spaces.\n- The fields are:\n1. Piece placement\n2. Active color\n3. Castling availability\n4. En passant target square\n5. Halfmove clock\n6. Fullmove number\n\n'''

        parse += default_string
        parse += self.get_piece_placement_text()
        parse += self.get_active_colour()
        parse += self.get_castling_availability()
        parse += self.get_en_passant_target()
        parse += self.get_halfmove_clock()
        parse += self.get_fullmove_number()
        parse += self.explain_board_state()
        parse += "Summary of the Board State:\n"
        parse += self.count_pieces()
        parse += "Piece Positions:\n"
        piece_positions_list = []
        for piece, positions in self.piece_positions.items():
            piece_positions_list.append(f"   - {piece}: {positions}\n")

        sorted_piece_positions_list = sorted(piece_positions_list, key=lambda x: x.strip()[2])
        for line in sorted_piece_positions_list:
            parse += line

        return parse

    def get_question_gt(self, analysis: str) -> (str, str, str):
        piece_positions_section = analysis.split("Piece Positions:\n")[-1]
        all_positions = piece_positions_section.split("\n")[:-1]
        target_position = random.choice(all_positions)
        piece = re.findall(r"\w+\s\w+", target_position)[0]
        gt = re.findall(r"[a-z]\d$", target_position)[0]
        question = f"Given a chess board state in the following FEN {self.fen} - what's the position of the {piece}?"
        return question, piece, gt

    @staticmethod
    def generate_answer_summary(piece, gt):
        return f"So, the position of {piece} is {gt}\n<ANSWER>: {gt}"

# if __name__ == "__main__":
#     fen = "1R6/p3k1p1/2p2b2/2Pn4/1BQPB3/P7/6PP/3q2K1 w - - 1 33"
#     chess_board = ChessBoard(fen)
#     print("\nDetailed FEN Analysis:")
#     print(chess_board.parse_fen_cot())
