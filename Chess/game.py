from agents.KeyboardAgent import KeyboardAgent
from chess import Board, WHITE, BISHOP


def runGame(args):
    board = Board()
    player1 = KeyboardAgent(board)
    player2 = args['agent'](board, args['depth'])

    currentPlayer = player1
    print('Start:')
    while not board.is_checkmate():
        print(board)
        print()
        move = currentPlayer.nextMove()

        if move not in board.legal_moves:
            raise Exception('Player did illegal move: ' + move)

        board.push(move)

        currentPlayer, toPrint = (player1, 'Player2:') if currentPlayer == player2 else (player2, 'Player1')
        print(toPrint)
