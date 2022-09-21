# Lab 1

### To test search algorithms use the following commands

### Lee Search:
- ```python pacman.py -l mediumMaze -p SearchAgent -a fn=leeSearch --goalX={int} --goalY={int}```
- goalX/Y are optional, by default (1, 1)

### Greedy Search:
- ```python pacman.py -l mediumMaze -p SearchAgent -a fn=greedySearch --goalX={int} --goalY={int}```

### A Star Search + Manhattan heuristic:
- ```python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --goalX={int} --goalY={int}```

### All Food Search:
- ```python pacman.py -l trickySearch -p AStarFoodSearchAgent```

### Corners Search:
- ```python pacman.py -l mediumCorners -p AStarCornersAgent```

### Note: You can customize mazes by modifying layouts