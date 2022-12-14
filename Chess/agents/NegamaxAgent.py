from agents.agents import HeuristicAgent
from chess import Board, Move


class NegamaxAgent(HeuristicAgent):

    def __init__(self, board, depth):
        super().__init__(board, depth)

    def nextMove(self):
        return self.__negamax(self.board, self.board.peek(), self.depth)[1]

    def __negamax(self, board: Board, move: Move, depth: int):
        if depth == 0 or board.is_checkmate():
            return self.evaluate(board), move

        maxScore = float('-inf')
        maxMove = None
        for legalMove in board.legal_moves:
            nextBoard = board.copy(stack=False)
            nextBoard.push(legalMove)
            successor = self.__negamax(nextBoard, legalMove, depth - 1)
            currentScore = -successor[0]
            if currentScore > maxScore:
                maxScore = currentScore
                maxMove = legalMove

        return maxScore, maxMove
