"""Given a chessboard with one K and one Q, see if the K can attack the Q.

This function is given coordinates for the king and queen on a chessboard.
These coordinates are given as a letter A-H for the columns and 1-8 for the
row (see below for example):

Queens can move in any direction: horizontally, vertically, or diagonally,
as far as possible.

This function returns True if the king is in the line of attack of the queen.

For example, these boards show the king under attack:

8    . . . . . . . .      . . . . . . . .      . . . . . . . .    8
7    . . . . . . . .      . . . . . . . .      . K . . . . . .    7
6    . . . K . . . Q      . . . . K . . .      . . . . . . . .    6
5    . . . . . . . .      . . . . . . . .      . . . Q . . . .    5
4    . . . . . . . .      . . . . Q . . .      . . . . . . . .    4
3    . . . . . . . .      . . . . . . . .      . . . . . . . .    3
2    . . . . . . . .      . . . . . . . .      . . . . . . . .    2
1    . . . . . . . .      . . . . . . . .      . . . . . . . .    1
     A B C D E F G H      A B C D E F G H      A B C D E F G H

     K=D6, Q=H6           K=E6, Q=E4           K=B7, Q=D5

>>> check("D6", "H6")
True

>>> check("E6", "E4")
True

>>> check("B7", "D5")
True

>>> check("A1", "H8")
True

>>> check("A8", "H1")
True

>>> check("D6", "H7")
False

>>> check("E6", "F4")
False
"""


def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    """

    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]

    if king[0] == queen[0]: # same column
        return True

    if king[1] == queen[1]: # same row
        return True

    queen_col = cols.index(queen[0])
    queen_row = rows.index(queen[1]) # might be unneccesary since index will always be row-1
    king_col = cols.index(king[0])
    king_row = rows.index(king[1])

    n = 1 # how far away from queen

    # only check within the board
    while queen_col-n >= 0 or queen_row-n >= 0 or queen_col+n < len(cols) or queen_row+n < len(rows):
        
        #-row, -col, bottom left corner
        # print("checking bottom left, col {}, row {}".format(queen_col-n, queen_row-n))
        if queen_col-n == king_col and queen_row-n == king_row:
            return True

        # +row, -col, top_left
        # print("checking top left")
        if queen_col-n == king_col and queen_row+n == king_row:
            return True

        # -row, + col, bottom_right
        # print("checking bottom right")
        if queen_col+n == king_col and queen_row-n == king_row:
            return True

        # +row, +col, top right
        # print("checking top right")
        if queen_col+n == king_col and queen_row+n == king_row:
            return True

        n+=1 # increment and move farther away from queen spot

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT GAME!\n")

