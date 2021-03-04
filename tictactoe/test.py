from functools import reduce
X = "X"
O = "O"
EMPTY = None

board =  [[EMPTY, "X", EMPTY],
            ["O", "O", "O"],
            ["X", "X", "O"]]




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

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check row bingo
    for i in range(3):
        symbol = board[i][0]
        cnt = 1
        for j in range(1,3):
            if board[i][j] != symbol: break
            cnt+=1
        if(cnt==3): return symbol  

    # check column bingo
    for j in range(3):
        symbol = board[0][j]
        cnt = 1
        for i in range(1,3):
            if board[i][j] != symbol :break
            cnt+=1
        if(cnt==3): return symbol

    # check diagonal bingo
    symbol = board[0][0]
    cnt = 1
    for i in range(1,3):           
        if board[i][i] != symbol : break
        cnt+=1
    if(cnt==3): return symbol  

    symbol = board[0][2]
    cnt = 1
    for i in range(1,3):           
        if board[i][2-i] != symbol : break
        cnt+=1
    if(cnt==3): return symbol    

    return None


print(winner(board))
print(X=="X")