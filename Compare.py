from GameState import GameState


def compareStates(firstState, secondState):
    first = GameState()
    second = GameState()
    first.loadLayoutFromFile(firstState)
    second.loadLayoutFromFile(secondState)
    for i, row in enumerate(first.game):
        for j, col in enumerate(row):
            if first.game[i][j] == second.game[i][j]:
                break
            elif first.game[i][j] != second.game[i][j]:
                print("False")
                return False
    print("True")
    return True


