from GameState import GameState


def normalize(gameBoard):
    # GameStates being created in too many files, how to fix this?
    game = GameState(gameBoard)
    game.board.normalize()
    game.printGame()
