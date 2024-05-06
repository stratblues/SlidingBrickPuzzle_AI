from Board import Board
from GameState import GameState
import Compare
import sys
import Normalize
import RandomWalk


def parseMove(moveArgument):
    moveArgument = moveArgument.strip("()")
    blockID, direction = moveArgument.split(",")
    blockID = int(blockID)
    direction = direction.strip()
    return blockID, direction


if __name__ == '__main__':
    command = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else None
    # GameStates being created in too many files, how to fix this?
    game = GameState(filename) if filename else GameState(None)
    if command == "print":
        game.printGame()
    elif command == "applyMove":
        move = sys.argv[3]
        blockID, direction = parseMove(move)
        game.applyMove(blockID, direction)
        game.printGame()
    elif command == "done":
        if game.identifySolutions():
            print("True")
        else:
            print("False")
    elif command == "availableMoves":
        moves = game.availableMoves()
        for move in moves:
            print(move)
    elif command == "compare":
        Compare.compareStates(sys.argv[2], sys.argv[3])
    elif command == "norm":
        Normalize.normalize(filename)
    elif command == "random":
        RandomWalk.randomWalk(filename, int(sys.argv[3]))
    elif command == "bfs":
        game.breadthFirstSearch()
    elif command == "dfs":
        game.depthFirstSearch()
    elif command == "ids":
        game.iterativeDeepeningSearch()
    elif command == "astar":
        game.aStarSearch()
