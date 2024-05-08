import random

from GameState import GameState


def randomWalk(filename, n):
    # GameStates being created in too many files, how to fix this?
    game = GameState(filename)
    game.printGame()
    print()
    count = 0
    for _ in range(n):
        availMoves = game.availableMoves()
        selectedMove = random.choice(availMoves)
        print(f"{selectedMove}")
        blockID, direction = selectedMove
        game.getBlock(blockID).move(direction, game.board)
        count += 1
        game.printGame()
        print()
        game.board.normalize()
        if game.board.identifySolutions():
            print(f"Game over, goal state reached in {count} move(s)!")
            return True
