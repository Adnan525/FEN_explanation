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
