from Board import Board
from GameState import GameState


def compareStates(firstFile, secondFile):
    # GameStates being created in too many files, how to fix this?
    firstState = GameState(firstFile)
    secondState = GameState(secondFile)

    # state comparison comes directly from the board, is this optimal?
    if firstState.board.compareStates(secondState.board):
        print("True")
        return True
    else:
        print("False")
        return False
