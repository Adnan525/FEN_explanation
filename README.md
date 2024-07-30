# Generate Chess Board State Explanation from FEN
Example input :  
```python
FEN = 4r1k1/1pR3p1/p2pn1qp/8/PPBP4/1QP1n3/3N2PP/5RK1 w - - 1 26
```
Board State :  
![FEN_setup](https://github.com/Adnan525/FEN_explanation/blob/master/fen_test.png)  
Output :  
```
Total 22 pieces present in the board

            White Pieces: 12 pieces which are 2 x White Rook, 6 x White Pawn, 1 x White Bishop, 1 x White Queen, 1 x White Knight, 1 x White King

            Black Pieces: 10 pieces which are 1 x Black Rook, 1 x Black King, 5 x Black Pawn, 2 x Black Knight, 1 x Black Queen
            
Board State is:
 1 1 1 1 r 1 k 1
 1 p R 1 1 1 p 1
 p 1 1 p n 1 q p
 1 1 1 1 1 1 1 1
 P P B P 1 1 1 1
 1 Q P 1 n 1 1 1
 1 1 1 N 1 1 P P
 1 1 1 1 1 R K 1

Piece Positions are:
Black Rook at e8
Black King at g8
Black Pawn at b7 g7 a6 d6 h6
White Rook at c7 f1
Black Knight at e6 e3
Black Queen at g6
White Pawn at a4 b4 d4 c3 g2 h2
White Bishop at c4
White Queen at b3
White Knight at d2
White King at g1
```
Output Updated [following CoT GPT 4]:
```
A FEN string is divided into six fields separated by spaces.
- The fields are:
1. Piece placement
2. Active color
3. Castling availability
4. En passant target square
5. Halfmove clock
6. Fullmove number

Piece Placement:
   - 4r1k1/1pR3p1/p2pn1qp/8/PPBP4/1QP1n3/3N2PP/5RK1
   - This represents the board from the 8th rank to the 1st rank.
   - Each rank is separated by a '/'.
   - Numbers represent empty squares, and letters represent pieces (uppercase for White, lowercase for Black)
Active Colour:
   - w indicates it is White's turn to move.
Castling Availability:
   - Neither side can castle.
En Passant Target Square:
   - There is no en passant target square.
Halfmove Clock:
   - The halfmove clock is 1. This is the number of halfmoves since the last pawn advance or capture.Fullmove Number:
   - The fullmove number is 26. This indicates that this is the 26th full move in the game.

Detailed Board State:
- 8th Rank: 4r1k1
  - 4 empty squares, Black Rook on e8, One empty square, Black King on g8, One empty square

- 7th Rank: 1pR3p1
  - One empty square, Black Pawn on b7, White Rook on c7, 3 empty squares, Black Pawn on g7, One empty square

- 6th Rank: p2pn1qp
  - Black Pawn on a6, 2 empty squares, Black Pawn on d6, Black Knight on e6, One empty square, Black Queen on g6, Black Pawn on h6

- 5th Rank: 8
  - 8 empty squares

- 4th Rank: PPBP4
  - White Pawn on a4, White Pawn on b4, White Bishop on c4, White Pawn on d4, 4 empty squares

- 3th Rank: 1QP1n3
  - One empty square, White Queen on b3, White Pawn on c3, One empty square, Black Knight on e3, 3 empty squares

- 2th Rank: 3N2PP
  - 3 empty squares, White Knight on d2, 2 empty squares, White Pawn on g2, White Pawn on h2

- 1th Rank: 5RK1
  - 5 empty squares, White Rook on f1, White King on g1, One empty square

Summary of the Board State:
   - Total 22 pieces present in the board
   - White Pieces: 12 pieces which are 2 x White Rook, 6 x White Pawn, 1 x White Bishop, 1 x White Queen, 1 x White Knight, 1 x White King
   - Black Pieces: 10 pieces which are 1 x Black Rook, 1 x Black King, 5 x Black Pawn, 2 x Black Knight, 1 x Black Queen
Piece Positions:
   - Black Rook: e8
   - Black King: g8
   - Black Pawn: b7 g7 a6 d6 h6
   - Black Knight: e6 e3
   - Black Queen: g6
   - White Rook: c7 f1
   - White Pawn: a4 b4 d4 c3 g2 h2
   - White Bishop: c4
   - White Queen: b3
   - White Knight: d2
   - White King: g1
```