from functools import reduce
X = "X"
O = "O"
EMPTY = None

board =  [[EMPTY, "X", EMPTY],
            ["O", "X", EMPTY],
            ["X", "O", "O"]]




def count(board, symbol):
    return reduce(lambda cnt, row:cnt+row.count(symbol), board, 0)    


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if count(board,X)==count(board,O) else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i,row in enumerate(board):
        for j,col in enumerate(row):

            if board[i][j] != EMPTY : continue
            actions.add((i,j))

    return actions    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    board[i][j] = player(board)
    return board


print(result(board, (0,0)))