from agents.agents import Agent
from chess import Move


class KeyboardAgent(Agent):

    def __init__(self, board):
        super().__init__(board)

    def nextMove(self):
        while True:
            uciMove = Move.from_uci(input('Enter uci move: '))
            print()
            if uciMove in self.board.legal_moves:
                return uciMove
