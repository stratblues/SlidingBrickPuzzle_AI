from GameState import GameState

board = GameState()


def normalize(gameBoard):
    board.loadLayoutFromFile(gameBoard)
    nextIdx = 3
    for i, row in enumerate(board.game):
        for j, col in enumerate(row):
            if board.game[i][j] == nextIdx:
                nextIdx = nextIdx + 1
            elif board.game[i][j] > nextIdx:
                swapIdx(nextIdx, board.game[i][j])
                nextIdx = nextIdx + 1
    board.printGame()


def swapIdx(idx1, idx2):
    for i, row in enumerate(board.game):
        for j, col in enumerate(row):
            if board.game[i][j] == idx1:
                board.game[i][j] = idx2
            elif board.game[i][j] == idx2:
                board.game[i][j] = idx1
