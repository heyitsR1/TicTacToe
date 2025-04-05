import tictactoe as ttt
from tictactoe import EMPTY
from tictactoe import X
from tictactoe import O

board_2 = [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board_3 = [[X, O, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board_4 = [[X, O, O],
            [O,O, O],
            [X, O, O]]

board = ttt.initial_state()

print (ttt.player(board))
print(ttt.result(board,(0,0)))
print(ttt.result(board_2,(0,1)))
print(ttt.winner(board_4))
print()


# print (ttt.actions(board))

# print (ttt.player(board_2))
# print (ttt.actions(board_2))

# print (ttt.player(board_3))
# print (ttt.actions(board_3))


