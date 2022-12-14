from chess import Board

from agents.agents import HeuristicAgent


class PVSAgent(HeuristicAgent):

    def nextMove(self):

        alpha = float('-inf')
        beta = float('inf')

        minScore = float('inf')
        move = None
        for legal_move in self.board.legal_moves:
            next_board = self.board.copy(stack=False)
            next_board.push(legal_move)
            score = self.__pvs(next_board, alpha, beta, 0)
            if score < minScore:
                minScore = score
                move = legal_move

        return move

    def __pvs(self, board: Board, alpha: float, beta: float, depth: int) -> float:
        if depth == self.depth or board.is_checkmate():
            return self.evaluate(board)

        searchPv = True

        for legal_move in board.legal_moves:
            next_board = board.copy(stack=False)
            next_board.push(legal_move)
            if searchPv:
                score = -self.__pvs(next_board, -beta, -alpha, depth + 1)
            else:
                score = -self.__pvs(next_board, -alpha - 1, -alpha, depth + 1)
                if score > alpha:
                    score = -self.__pvs(next_board, -beta, -alpha, depth + 1)

            if score >= beta:
                return beta

            if score > alpha:
                alpha = score
                searchPv = False

        return alpha
