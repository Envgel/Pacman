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
# student id 978308
# sutdent name: ling fang

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


def depthFirstSearch(problem):
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
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    # open_list = util.Stack()
    # close_list = []
    # open_list.push((problem.getStartState(), [], 0))
    # while not open_list.isEmpty():
    #     (state, toDirection, toCost) = open_list.pop()
    #     if state not in close_list:
    #         close_list.append(state)
    #     if problem.isGoalState(state):
    #         return toDirection
    #     for successor, action, stepCost in problem.getSuccessors(state):
    #         open_list.push((successor, toDirection + [action], toCost + stepCost))
    pass


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    open_list = util.Queue()
    close_list = []
    open_list.push((problem.getStartState(), [], 0))
    shortest_to_start = {}
    while not open_list.isEmpty():
        (state, toDirection, toCost) = open_list.pop()
        if problem.isGoalState(state):
            return toDirection
        if state not in close_list or toCost < shortest_to_start[state]:
            close_list.append(state)
            shortest_to_start[state] = toCost
            for successor, action, stepCost in problem.getSuccessors(state):
                shortest_to_start[state] = toCost
                open_list.push((successor, toDirection + [action], toCost + stepCost))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    pass


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    open_list = util.PriorityQueue()
    close_list = []
    best_g = {}  # maps states to numbers
    open_list.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))

    while not open_list.isEmpty():
        (state, toDirection, toCost) = open_list.pop()  # get best state
        if state not in close_list or toCost < best_g[state]:
            close_list.append(state)
            best_g[state] = toCost
            if problem.isGoalState(state) == True:
                return toDirection
            # expand state
            for successor, action, stepCost in problem.getSuccessors(state):
                h_cost = heuristic(successor, problem) + stepCost + toCost
                open_list.push((successor, toDirection + [action], stepCost + toCost), h_cost)


def iterativeDeepeningSearch(problem):
    max_depth = 1
    actions = []
    while not actions:
        actions = iterativeDFS(problem, max_depth)
        max_depth += 1
    return actions


def iterativeDFS(problem, max_depth):
    open_list = util.Stack()
    close_list = []
    open_list.push((problem.getStartState(), [], 0))
    best = {}
    while not open_list.isEmpty():
        (state, toDirection, toCost) = open_list.pop()
        if problem.isGoalState(state):
            return toDirection
        if (state not in close_list) or toCost < best[state]:
            if toCost <= max_depth:
                best[state] = toCost
                close_list.append(state)
                for successor, action, stepCost in problem.getSuccessors(state):
                    open_list.push((successor, toDirection + [action], toCost + stepCost))


def waStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has has the weighted (x 2) lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE FOR TASK 2 ***"
    open_list = util.PriorityQueue()
    close_list = []
    best_g = {}  # maps states to numbers
    open_list.push((problem.getStartState(), [], 0), 2 * heuristic(problem.getStartState(), problem))

    while not open_list.isEmpty():
        (state, toDirection, toCost) = open_list.pop()  # get best state
        # re-open if betterg; note that allσ′with same state
        # but worsegarebehindσinopen,
        # and will be skipped when their turn comes
        if state not in close_list or toCost < best_g[state]:
            close_list.append(state)
            best_g[state] = toCost
            if problem.isGoalState(state):
                return toDirection
            # expand state
            for successor, action, stepCost in problem.getSuccessors(state):
                h_cost = 2 * heuristic(successor, problem) + stepCost + toCost
                open_list.push((successor, toDirection + [action], stepCost + toCost), h_cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
wastar = waStarSearch
