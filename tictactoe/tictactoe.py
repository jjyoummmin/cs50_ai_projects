"""
Tic Tac Toe Player
"""

import math
from functools import reduce

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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
    actions = []
    for i,row in enumerate(board):
        for j,col in enumerate(row):

            if board[i][j] != EMPTY : continue
            actions.append((i,j))

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
            cnt++
        if(cnt==3) return symbol  

    # check column bingo
    for j in range(3):
        symbol = board[0][j]
        cnt = 1
        for i in range(1,3):
            if board[i][j] != symbol :break
            cnt++
        if(cnt==3) return symbol

    # check diagonal bingo
    symbol = board[0][0]
    cnt = 1
    for i in range(1,3):           
        if board[i][i] != symbol : break
        cnt++
    if(cnt==3) return symbol  

    symbol = board[0][2]
    cnt = 1
    for i in range(1,3):           
        if board[i][2-i] != symbol : break
        cnt++
    if(cnt==3) return symbol    

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
