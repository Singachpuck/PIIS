# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from searchAgents import CornersProblem, PositionSearchProblem

    if isinstance(problem, CornersProblem):
        result = []
        s = problem.getStartState()
        for corner in problem.combination:
            result += aStarSearch(PositionSearchProblem(problem.gameState, goal=problem.corners[corner], start=s))
            s = problem.corners[corner]
        return result

    processed = []
    stateQueue = util.PriorityQueue()

    startState = problem.getStartState()
    stateQueue.push((startState, [], 0), 0)

    while not stateQueue.isEmpty():
        currentState = stateQueue.pop()
        processed.append(currentState[0])
        if problem.isGoalState(currentState[0]):
            return currentState[1]

        for successor in problem.getSuccessors(currentState[0]):
            state = successor[0]
            if state not in processed:
                toQueue = (state, currentState[1] + [successor[1]], currentState[2] + successor[2])
                stateQueue.update(toQueue, toQueue[2] + heuristic(successor[0], problem))

    raise RuntimeError('Final state is not reachable!')

def greedySearch(problem: SearchProblem):

    from searchAgents import manhattanHeuristic

    path = []
    processed = []

    current = problem.getStartState()
    processed.append(current)

    while not problem.isGoalState(current):
        availableSuccessors = [s for s in problem.getSuccessors(current) if s[0] not in processed]

        if len(availableSuccessors) == 0:
            if len(path) == 0:
                raise RuntimeError('Final state is not reachable!')

            path.pop()
            current = path[len(path) - 1][0] if len(path) != 0 else problem.getStartState()
            continue

        minSuccessor = min(availableSuccessors, key=lambda s: manhattanHeuristic(s[0], problem))

        path.append((minSuccessor[0], minSuccessor[1]))
        processed.append(minSuccessor[0])
        current = minSuccessor[0]

    return list(map(lambda pi: pi[1], path))

def leeSearch(problem: SearchProblem):

    startState = problem.getStartState()
    stateCounter = util.Counter()
    queue = util.Queue()
    queue.push(startState)
    stateCounter[startState] = 0

    def rollback(curState, resultPath=[]):
        if stateCounter[curState] == 0:
            return resultPath

        for s in problem.getSuccessors(curState):
            adjacentState = s[0]
            if adjacentState in stateCounter and stateCounter[adjacentState] == stateCounter[curState] - 1:
                resultPath.insert(0, Directions.REVERSE[s[1]])
                return rollback(adjacentState)

        raise AttributeError('Wrong final state, can\'t find path back!')

    while not queue.isEmpty():
        currentState = queue.pop()

        if problem.isGoalState(currentState):
            return rollback(currentState)

        for successor in problem.getSuccessors(currentState):
            if successor[0] not in stateCounter:
                stateCounter[successor[0]] = stateCounter[currentState] + 1
                queue.push(successor[0])

    raise RuntimeError('Final state is not reachable!')

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
