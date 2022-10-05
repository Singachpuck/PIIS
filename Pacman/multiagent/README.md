# Lab 2

### To test search algorithms use the following commands

### Minimax with alpha-beta pruning
- ``python pacman.py -p AlphaBetaAgent -a depth=3,evalFn=better -l mediumClassic -g RandomGhost,DirectionalGhost -k 2``

### Expectimax
- ``python pacman.py -p ExpectimaxAgent -a depth=3,evalFn=better -l mediumClassic -g RandomGhost,DirectionalGhost -k 2``

## You can specify as many ghosts as you need, but you also have to place this ghost into the layout (don't forget to update -k option)