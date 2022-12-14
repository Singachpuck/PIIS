# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def alphaBetaPrunning(gameState,agent,depth,a,b):
            actions = gameState.getLegalActions(agent)
            if not actions or depth == self.depth:
                return self.evaluationFunction(gameState),0

            if agent == gameState.getNumAgents() - 1:
                nextAgent = self.index
                depth += 1
            else:
                nextAgent = agent + 1

            bestOption = []
            for action in actions:
                if not bestOption:
                    next = alphaBetaPrunning(gameState.generateSuccessor(agent,action),nextAgent,depth,a,b)

                    bestOption.append(next[0])
                    bestOption.append(action)

                    if agent == self.index:
                        a = max(bestOption[0],a)
                    else:
                        b = min(bestOption[0],b)
                else:
                    if bestOption[0] > b and agent == self.index:
                        return bestOption

                    if bestOption[0] < a and agent != self.index:
                        return bestOption

                    previousValue = bestOption[0]
                    next = alphaBetaPrunning(gameState.generateSuccessor(agent,action),nextAgent,depth,a,b)

                    if agent == self.index:
                        if next[0] > previousValue:
                            bestOption[0] = next[0]
                            bestOption[1] = action

                            a = max(bestOption[0],a)
                    else:
                        if next[0] < previousValue:
                            bestOption[0] = next[0]
                            bestOption[1] = action

                            b = min(bestOption[0],b)
            return bestOption

        alpha, beta = -float("inf"),float("inf")
        return alphaBetaPrunning(gameState,self.index,0,alpha,beta)[1]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(gameState, depth, agent):
            actions = gameState.getLegalActions(agent)
            if not actions or depth == 0 or gameState.isWin() or gameState.isLose():
                return (self.evaluationFunction(gameState), '')

            if agent == gameState.getNumAgents() - 1:
                depth -= 1

            if agent == 0:
                bestOption = -float('inf')
            else:
                bestOption = 0
            bestAction = ''
            next = (agent + 1) % gameState.getNumAgents()
            for action in actions:
                result = expectimax(gameState.generateSuccessor(agent, action), depth, next)

                if agent == 0:
                    if result[0] > bestOption:
                        bestOption = result[0]
                        bestAction = action
                else:
                    bestOption += 1.0 / len(actions) * result[0]
                    bestAction = action
            return (bestOption, bestAction)

        return expectimax(gameState, self.depth, 0)[1]

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    foodList = currentGameState.getFood().asList()
    ghosts = currentGameState.getGhostStates()
    pacmanPosition = currentGameState.getPacmanPosition()
    activeGhosts = []
    scaredGhosts = []
    totalCapsules = len(currentGameState.getCapsules())
    totalFood = len(foodList)
    heuristicValue = 0

    for ghost in ghosts:
        if ghost.scaredTimer:
            scaredGhosts.append(ghost)
        else:
            activeGhosts.append(ghost)

    heuristicValue += 1.5 * currentGameState.getScore()
    heuristicValue += -10 * totalFood
    heuristicValue += -20 * totalCapsules

    foodDistances = []
    activeGhostsDistances = []
    scaredGhostsDistances = []

    for food in foodList:
        foodDistances.append(manhattanDistance(pacmanPosition, food))

    for ghost in activeGhosts:
        scaredGhostsDistances.append(manhattanDistance(pacmanPosition, ghost.getPosition()))

    for ghost in scaredGhosts:
        scaredGhostsDistances.append(manhattanDistance(pacmanPosition, ghost.getPosition()))

    for distance in foodDistances:
        if distance < 3:
            heuristicValue += -1 * distance
        if distance < 7:
            heuristicValue += -0.5 * distance
        else:
            heuristicValue += -0.2 * distance

    for distance in scaredGhostsDistances:
        if distance < 3:
            heuristicValue += -20 * distance
        else:
            heuristicValue += -10 * distance

    for distance in activeGhostsDistances:
        if distance < 3:
            heuristicValue += 3 * distance
        elif distance < 7:
            heuristicValue += 2 * distance
        else:
            heuristicValue += 0.5 * distance

    return heuristicValue

# Abbreviation
better = betterEvaluationFunction
