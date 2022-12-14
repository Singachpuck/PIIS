from agents.agents import HeuristicAgent
from chess import Board, Move


class NegaScoutAgent(HeuristicAgent):

    def __init__(self, board, depth):
        super().__init__(board, depth)

    def nextMove(self) -> Move:
        alpha = float('-inf')
        beta = float('inf')

        minScore = float('inf')
        move = None
        for legal_move in self.board.legal_moves:
            next_board = self.board.copy(stack=False)
            next_board.push(legal_move)
            score = self.__negascout(next_board, alpha, beta, 0)
            if score < minScore:
                minScore = score
                move = legal_move

        return move

    def __negascout(self, board: Board, alpha: float, beta: float, depth: int) -> float:
        if depth == self.depth or board.is_checkmate():
            return self.evaluate(board)

        is_first = True
        a = alpha
        b = beta
        for legal_move in board.legal_moves:
            next_board = board.copy(stack=False)
            next_board.push(legal_move)
            score = -self.__negascout(next_board, -b, -a, depth + 1)
            if (score > a) and (score < beta) and not is_first and depth < self.depth - 1:
                a = -self.__negascout(next_board, -beta, -score, depth + 1)

            a = max(a, score)

            if a >= beta:
                return a

            b = a + 1
            is_first = False

        return a
