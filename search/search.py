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

class State:

    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        # G is the distance between the current node and the start node.
        self.g = 0
        # H is the heuristic estimated distance from the current node to the end node.
        self.h = 0
        # F is the total cost of the node.
        self.f = 0

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
    # util.raiseNotDefined()


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

# def breadthFirstSearch(problem):
#     """Search the shallowest nodes in the search tree first."""
#     "*** YOUR CODE HERE ***"
#
#     fringe = util.Queue()
#     # Just location, like [7, 7]
#     startLocation = problem.getStartState()
#     # (location, path)
#     startNode = (startLocation, [])
#     fringe.push(startNode)
#     visitedLocation = set()
#     visitedLocation.add(startLocation)
#
#     while not fringe.isEmpty():
#         # node[0] is location, while node[1] is path
#         node = fringe.pop()
#         if problem.isGoalState(node[0]):
#             return node[1]
#         successors = problem.getSuccessors(node[0])
#         for item in successors:
#             if item[0] in visitedLocation:
#                 continue
#             visitedLocation.add(item[0])
#             fringe.push((item[0], node[1] + [item[1]]))
#
#     return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "*** YOUR CODE HERE ***"
    # Get start state
    start_state = State(None, problem.getStartState())
    # A queue to store the states
    queue = util.Queue()
    queue.push(start_state)
    checkedPath = set()
    checkedPath.add(start_state.position)
    while not queue.isEmpty():
        current_state = queue.pop()
        # print "current_state:", current_state.position
        # print "Is current a goal?", problem.isGoalState(current_state.position)
        # print "Successors:", problem.getSuccessors(current_state.position)
        if problem.isGoalState(current_state.position):
            current = current_state
            path = []
            while current is not None:
                path.append(current.position)
                current = current.parent
            return getPathSet(problem, path[::-1])  # Return reversed path

        for successor in problem.getSuccessors(current_state.position):
            # no cycle
            # print(successor[0])
            if successor[0] in checkedPath:
                continue
            checkedPath.add(successor[0])
            queue.push(State(current_state, successor[0]))

def uniformCostSearch(problem):
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    queue = util.PriorityQueue()

    start_state = State(None, problem.getStartState())
    # print(start_state.position)
    start_state.g = 0

    queue.update(start_state, 1)

    state_list = {start_state.position: start_state}
    while queue:
        current_state = queue.pop()
        print "current_state:", current_state.position
        print "Is current a goal?", problem.isGoalState(current_state.position)
        print "Successors:", problem.getSuccessors(current_state.position)
        if problem.isGoalState(current_state.position):
            print(" Goal!!!", current_state.position)
            path = []
            current = current_state
            while current is not None:
                path.append(current.position)
                current = current.parent
            return getPathSet(problem, path[::-1])  # Return reversed path
        elif len(problem.getSuccessors(current_state.position)) == 0:
            return False
        else:
            for successor in problem.getSuccessors(current_state.position):
                successor_state = State(current_state, successor[0])
                successor_state.g = successor[2] + current_state.g
                if successor_state.position not in state_list or state_list.get(
                        successor_state.position).g > successor_state.g:
                    state_list[successor_state.position] = successor_state
                    queue.update(successor_state, successor_state.g)



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()

    start_state = State(None, problem.getStartState())
    # print(start_state.position)
    start_state.g = 0
    start_state.h = heuristic(start_state.position, problem)
    start_state.f = start_state.g + start_state.h

    queue.update(start_state, 1)

    state_list = {start_state.position: start_state}
    while queue:
        current_state = queue.pop()
        print "current_state:", current_state.position
        print "Is current a goal?", problem.isGoalState(current_state.position)
        print "Successors:", problem.getSuccessors(current_state.position)
        if problem.isGoalState(current_state.position):
            print(" Goal!!!", current_state.position)
            path = []
            current = current_state
            while current is not None:
                path.append(current.position)
                current = current.parent
            return getPathSet(problem, path[::-1])   # Return reversed path
        elif len(problem.getSuccessors(current_state.position)) == 0:
            return False
        else:
            for successor in problem.getSuccessors(current_state.position):
                successor_state = State(current_state, successor[0])
                successor_state.g = successor[2] + current_state.g
                successor_state.h = heuristic(start_state.position, problem)
                successor_state.f = successor_state.g + successor_state.h
                if successor_state.position not in state_list or state_list.get(successor_state.position).f > successor_state.f:
                    state_list[successor_state.position] = successor_state
                    queue.update(successor_state, successor_state.f)

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
