import sys
import game
from argumentsParser import parseArguments

if __name__ == '__main__':

    args = parseArguments(sys.argv[1:])
    game.runGame(args)
