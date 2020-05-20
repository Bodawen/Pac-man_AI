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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


from game import Directions

s = Directions.SOUTH
w = Directions.WEST
n = Directions.NORTH
e = Directions.EAST
import util


def getDirection(d):
    if d == 'North':
        return n
    elif d == 'East':
        return e
    elif d == 'West':
        return w
    elif d == 'South':
        return s
    else:
        exit("False direction")


def getPathSet(problem, stack):
    path = []
    for i in range(len(stack) - 1):
        for succ in problem.getSuccessors(stack[i]):
            if succ[0] == stack[i + 1]:
                direction = succ[1]
                path.append(getDirection(direction))
                break
    print(path)
    return path


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "*** YOUR CODE HERE ***"
    # Get start state
    start_state = problem.getStartState()
    # Check if the initiate state is goal state.
    if problem.isGoalState(start_state):
        return []
    # A stack to store all possible states
    myStack = [problem.getStartState()]
    for successor in problem.getSuccessors(problem.getStartState()):
        myStack.append(successor[0])
        isGoal, reStack = depthFirstSearch_recursion(problem, myStack)
        if isGoal:
            print("get goal!")
            path = getPathSet(problem, reStack)
            print("The path is:", reStack)
            return path
        else:
            print("No goal!")
    util.raiseNotDefined()


def depthFirstSearch_recursion(problem, stack):
    current_state = stack[-1]
    print "current_state:", current_state
    print "Is current a goal?", problem.isGoalState(current_state)
    print "Successors:", problem.getSuccessors(current_state)
    if problem.isGoalState(current_state):
        return True, stack
    elif len(problem.getSuccessors(current_state)) == 0:
        return False, stack
    else:
        for successor in problem.getSuccessors(current_state):
            if successor[0] in stack:
                continue
            stack.append(successor[0])
            isGoal, reStack = depthFirstSearch_recursion(problem, stack)
            if isGoal:
                return isGoal, reStack
        stack.pop()
        return False, stack


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "*** YOUR CODE HERE ***"
    # Get start state
    start_state = problem.getStartState()
    # A queue to store the states
    queue = [(start_state, start_state)]
    checkedPath = [start_state[0]]
    isGoal, path = breadthFirstSearch_recursion(problem, queue, checkedPath)
    if isGoal:
        print("get Goal", path[:-1])
        path = path[:-1][::-1]
        return getPathSet(problem, path)
    else:
        print "No goal"
    util.raiseNotDefined()

def breadthFirstSearch_recursion(problem, queue, checkedPath):
    print(queue)
    paar_states = queue.pop()
    current_state = paar_states[0]
    parent_state = paar_states[1]

    print "current_state:", current_state
    print "Is current a goal?", problem.isGoalState(current_state)
    print "Successors:", problem.getSuccessors(current_state)
    # check goal
    if problem.isGoalState(current_state):
        path = [current_state, parent_state]
        print "Get Goal!!!", current_state
        return True, path
    # check wrong way
    elif len(problem.getSuccessors(current_state)) == 0:
        return False, []
    else:
        checkedPath.append(current_state)
        for successor in problem.getSuccessors(current_state):
            # no cycle
            if successor[0] in checkedPath:
                continue
            queue.insert(0, (successor[0], current_state))

    isGoal, path = breadthFirstSearch_recursion(problem, queue, checkedPath)
    if isGoal:
        if path[-1] == current_state:
            path.append(parent_state)
            return True, path
        else:
            return True, path
    else:
        return False, []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
