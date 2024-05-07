import sys

import Compare
import Normalize
import RandomWalk
from AstarSearch import AstarSearch
from BreadthFirstSearch import BreadthFirstSearch
from DepthFirstSearch import DepthFirstSearch
from GameState import GameState
from IterativeDeepeningSearch import IterativeDeepeningSearch


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
        search = BreadthFirstSearch()
        search.search(game)
    elif command == "dfs":
        search = DepthFirstSearch()
        search.search(game)
    elif command == "ids":
        search = IterativeDeepeningSearch()
        search.search(game)
    elif command == "astar":
        search = AstarSearch()
        search.search(game)
