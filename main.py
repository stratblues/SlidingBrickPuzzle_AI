from GameState import GameState
import Compare
import sys

if __name__ == '__main__':
    game = GameState()

    command = sys.argv[1]
    game.loadLayoutFromFile(sys.argv[2])
    if command == "print":
        game.printGame()
    elif command == "applyMove":
        game.applyMove(sys.argv[3])
        game.printGame()
    elif command == "done":
        game.identifySolutions()
    elif command == "availableMoves":
        game.printAllMoves()
    elif command == "compare":
        Compare.compareStates(sys.argv[2], sys.argv[3])
