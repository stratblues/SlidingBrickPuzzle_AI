from GameState import GameState
import sys

if __name__ == '__main__':
    game = GameState()
    game.loadLayoutFromFile(sys.argv[2])
    game.returnNewStateAfterMove(sys.argv[3])
