from chess import engine
from chess import Board, Move, Square, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, WHITE, BLACK, SquareSet, BaseBoard, Piece


class Agent:

    def __init__(self, board: Board):
        self.board = board

    def nextMove(self):
        raise NotImplementedError()


class HeuristicAgent(Agent):

    NORTH = 1
    NORTH_EAST = 2
    EAST = 3
    SOUTH_EAST = 4
    SOUTH = 5
    SOUTH_WEST = 6
    WEST = 7
    NORTH_WEST = 8

    pieces_direction = {
        BISHOP: [NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST],
        ROOK: [NORTH, EAST, SOUTH, WEST],
        QUEEN: [NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST, NORTH, EAST, SOUTH, WEST]
    }

    directions = ['NORTH', 'NORTH-EAST', 'EAST', 'SOUTH-EAST', 'SOUTH', 'SOUTH-WEST', 'WEST', 'NORTH-WEST']

    def __init__(self, board: Board, depth: int):
        super().__init__(board)
        self.depth = depth
        self.e = engine.SimpleEngine.popen_uci("stockfish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")

    def __del__(self):
        self.e.quit()

    def evaluate(self, board: Board) -> float:
        info = self.e.analyse(board, engine.Limit(depth=self.depth))

        # print(info["score"].relative.score(mate_score=10_000_000))

        return info["score"].pov(color=BLACK).score(mate_score=10_000_000)
    #
    # def evaluate(self, board: Board) -> float:
    #     def is_valid(sq: int):
    #         rank, file = chess.square_rank(sq), chess.square_file(sq)
    #         valid = True
    #         if rank < 0:
    #             valid = False
    #         if rank > 7:
    #             valid = False
    #         if file < 0:
    #             valid = False
    #         if file > 7:
    #             valid = False
    #         return valid
    #
    #     def trim(sq: int):
    #         rank, file = chess.square_rank(sq), chess.square_file(sq)
    #         if rank < 0:
    #             rank = 0
    #         if rank > 7:
    #             rank = 7
    #         if file < 0:
    #             file = 0
    #         if file > 7:
    #             file = 7
    #         return chess.square(file, rank)
    #
    #     def getValidMoves(initialSq, coefX, coefY):
    #         rank, file = chess.square_rank(initialSq), chess.square_file(initialSq)
    #         moves = []
    #
    #         while True:
    #             file += coefX
    #             rank += coefY
    #
    #             if not is_valid(chess.square(file, rank)):
    #                 return moves
    #
    #             newSq = board.piece_at(chess.square(file, rank))
    #             if newSq is not None:
    #                 return moves
    #
    #             moves.append((rank, file))
    #
    #     def getLegalMovesOfPiece(sq: int, piece: int):
    #         rank, file = chess.square_rank(sq), chess.square_file(sq)
    #         if piece == KNIGHT:
    #             moves = filter(lambda i: is_valid(chess.square(i[1], i[0])) and board.piece_at(chess.square(i[1], i[0])) is None,
    #                    [(rank + 2, file + 1),
    #                      (rank + 1, file + 2),
    #                      (rank - 1, file + 2),
    #                      (rank - 2, file + 1),
    #                      (rank - 2, file - 1),
    #                      (rank - 1, file - 2),
    #                      (rank + 1, file - 2),
    #                      (rank + 2, file - 1)])
    #
    #             return moves
    #         if piece == BISHOP:
    #             moves = getValidMoves(sq, 1, 1) + getValidMoves(sq, 1, -1) + getValidMoves(sq, -1, 1) + getValidMoves(sq, -1, -1)
    #             return moves
    #         if piece == ROOK:
    #             moves = getValidMoves(sq, 1, 0) + getValidMoves(sq, 0, 1) + getValidMoves(sq, -1, 0) + getValidMoves(sq, 0, -1)
    #             return moves
    #         if piece == QUEEN:
    #             moves = getValidMoves(sq, 1, 1) + getValidMoves(sq, 1, -1) + getValidMoves(sq, -1, 1) + getValidMoves(sq, -1, -1) + \
    #                     getValidMoves(sq, 1, 0) + getValidMoves(sq, 0, 1) + getValidMoves(sq, -1, 0) + getValidMoves(sq, 0, -1)
    #             return moves
    #
    #     if board.is_checkmate():
    #         board.turn
    #
    #     PAWN_VALUE = 1000
    #     KNIGHT_VALUE = 3100
    #     BISHOP_VALUE = 3200
    #     ROOK_VALUE = 5000
    #     QUEEN_VALUE = 9000
    #     KING_VALUE = 100_000
    #
    #     heuristic = 0
    #
    #     pawns = board.pieces(PAWN, BLACK)
    #     knights = board.pieces(KNIGHT, BLACK)
    #     bishops = board.pieces(BISHOP, BLACK)
    #     rooks = board.pieces(ROOK, BLACK)
    #     queens = board.pieces(QUEEN, BLACK)
    #     kings = board.pieces(KING, BLACK)
    #
    #     heuristic += len(pawns) * PAWN_VALUE
    #     heuristic += len(knights) * KNIGHT_VALUE
    #     heuristic += len(bishops) * BISHOP_VALUE
    #     heuristic += len(rooks) * ROOK_VALUE
    #     heuristic += len(queens) * QUEEN_VALUE
    #     heuristic += len(kings) * KING_VALUE
    #
    #     # for queen in queens:
    #     #     heuristic += sum(map(lambda pawn: 5, getLegalMovesOfPiece(queen, QUEEN)))
    #     # for rook in rooks:
    #     #     heuristic += sum(map(lambda pawn: 5, getLegalMovesOfPiece(rook, ROOK)))
    #     #     heuristic += 20 if chess.square_rank(rook) == 6 else 0
    #     #
    #     #     rookRank = chess.square_rank(rook)
    #     #     rookFile = chess.square_file(rook)
    #     #
    #     #     heuristic -= 10 if (rookFile == 7 or board.piece_at(chess.square(rookFile + 1, rookRank)) is not None)\
    #     #                        and (rookFile == 0 or board.piece_at(chess.square(rookFile - 1, rookRank)) is not None)\
    #     #         else 0
    #     #
    #     #     heuristic += 30 if (rookFile != 7 and board.piece_at(chess.square(rookFile + 1, rookRank)) is None)\
    #     #                        and (rookFile != 0 and board.piece_at(chess.square(rookFile - 1, rookRank)) is None)\
    #     #         else 0
    #     # for bishop in bishops:
    #     #     heuristic += sum(map(lambda p: 5, getLegalMovesOfPiece(bishop, BISHOP)))
    #     # for knight in knights:
    #     #     heuristic += sum(map(lambda p: 5, getLegalMovesOfPiece(knight, KNIGHT)))
    #     # for pawn in pawns:
    #     #     pawnRank = chess.square_rank(pawn)
    #     #     pawnFile = chess.square_file(pawn)
    #     #     heuristic += 10 if pawnRank in (3, 4) and pawnFile in (3, 4) else 0
    #     #
    #     #     for king in kings:
    #     #         kingFile = chess.square_file(king)
    #     #         kingRank = chess.square_rank(king)
    #     #         successorCells = [(min(kingRank + 1, 7), kingFile),
    #     #                           (min(kingRank + 1, 7), min(kingFile + 1, 7)),
    #     #                           (kingRank, min(kingFile + 1, 7)),
    #     #                           (max(kingRank - 1, 0), min(kingFile + 1, 7)),
    #     #                           (max(kingRank - 1, 0), kingFile),
    #     #                           (max(kingRank - 1, 0), max(kingFile - 1, 0)),
    #     #                           (kingRank, max(kingFile - 1, 0)),
    #     #                           (min(kingRank + 1, 7), max(kingFile - 1, 0))]
    #     #         heuristic += 9 if (pawnRank, pawnFile) in successorCells else 0
    #
    #             # for square in map(lambda cell: chess.square(cell[1], cell[0]), successorCells):
    #             #     heuristic += -30 if board.is_attacked_by(WHITE, square) else 0
    #             #     heuristic += 25 if board.color_at(square) is not None and board.color_at(square) == WHITE else 0
    #
    #     return -heuristic
