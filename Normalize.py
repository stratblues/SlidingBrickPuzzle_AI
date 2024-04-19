from GameState import GameState


def normalize(gameBoard):
    game = GameState(gameBoard)
    game.board.normalize(game.board)
    game.printGame()
