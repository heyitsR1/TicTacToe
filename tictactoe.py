"""
Tic Tac Toe Player
"""

import math
import copy
import math

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    # print (board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError
    board_copy = copy.deepcopy(board)
    # print (board)
    # print (*action)

    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # diag check
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] != EMPTY:
            return board[1][1]
    # column check
    if (board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY):
        return board[0][0]
    if (board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY):
        return board[0][1]
    if (board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY):
        return board[0][2]

    # row check
    if (board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY):
        return board[0][0]
    if (board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY):
        return board[1][0]
    if (board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY):
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    if terminal(board):
        return None
    current_player = player(board)

    if current_player == X:
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            score = MinValue(result(board, action))
            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    else:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            score = MaxValue(result(board, action))
            if score < best_score:
                best_score = score
                best_move = action
        return best_move

    """
    Returns the optimal action for the current player on the board.
    """


def MaxValue(board):
    if terminal(board):
        return utility(board)
    v = - math.inf
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v


def MinValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v
