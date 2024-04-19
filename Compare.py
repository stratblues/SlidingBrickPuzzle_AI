from Board import Board
from GameState import GameState


def compareStates(firstFile, secondFile):
    firstState = GameState(firstFile)
    secondState = GameState(secondFile)

    if firstState.board.compareStates(secondState.board):
        print("True")
        return True
    else:
        print("False")
        return False


