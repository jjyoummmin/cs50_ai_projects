"""
Tic Tac Toe Player
"""

import math
from functools import reduce
import copy

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
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


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



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or count(board,EMPTY)==0



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w==X : return 1 
    else : return -1 if w==O else 0 

def max_value(board):
    if(terminal(board)): 
        return (None,utility(board))
    v = -math.inf  
    max_action = None;
    for action in actions(board):
        min_val = min_value(result(board,action))[1]
        if v >= min_val : continue
        else :
            max_action = action
            v = min_val 
    return (max_action, v)    

def min_value(board):
    if(terminal(board)): 
        return (None,utility(board))
    v = math.inf  
    min_action = None;
    for action in actions(board):
        max_val = max_value(result(board,action))[1]
        if v <= max_val : continue
        else :
            min_action = action
            v = max_val 
    return (min_action, v) 

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return max_value(board)[0] if player(board) == X else min_value(board)[0] 

