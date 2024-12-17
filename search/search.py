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
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    start = problem.getStartState() #returns the start state
    target = problem.isGoalState(start) # checking if start is a goal
    stack_ = util.Stack()
    visited = set()
    
    stack_.push((start, [])) #(node,actions)
    #visited.add(start)
    
    if start == target:
        return [] # retrun a list of actions (empty, no path available)
    
    while not stack_.isEmpty():
        #pop from the stack 
        currNode, curr_actions = stack_.pop()
        if currNode not in visited:
            visited.add(currNode)
            if problem.isGoalState(currNode): # once the current node reached the goal, return the actions 
                return curr_actions
            # get the next set of actions from the getsuccessor method, (successor, action, stepCost)
            for nextMove, action, _ in problem.getSuccessors(currNode): #don't need the cost here, just putting a placeholder
                if nextMove not in visited:
                    new_actions = curr_actions + [action] #updates the move and the actions.
                    stack_.push((nextMove,new_actions))    
            # note: the new actions created during the push will be the current actions during the pop, that's why we need to keep it as a list. 
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState() #returns the start state
    target = problem.isGoalState(start) # checking if start is a goal
    queue_ = util.Queue()
    #visited = set()
    visited = []
    
    queue_.push((start, [])) #(node,actions)
    
    if start == target:
        return [] # retrun a list of actions (empty, no path available)
    
    while not queue_.isEmpty():
        #pop from the stack 
        currNode, curr_actions = queue_.pop()
        if currNode not in visited:
            visited.append(currNode)
            if problem.isGoalState(currNode): # once the current node reached the goal, return the actions 
                return curr_actions
            # get the next set of actions from the getsuccessor method, (successor, action, stepCost)
            for nextMove, action, _ in problem.getSuccessors(currNode): #don't need the cost here, just putting a placeholder
                if nextMove not in visited:
                    new_actions = curr_actions + [action] #updates the move and the actions.
                    queue_.push((nextMove,new_actions)) 
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    start = problem.getStartState() #returns the start state
    target = problem.isGoalState(start) # checking if start is a goal
    visited = set()
    priority_queue.push((start,[],0),0) #(state,action,cost)priority. cost and priority are first set to 0.
    if start == target:
        return []
    while not priority_queue.isEmpty():
        currNode, curr_actions, currCost = priority_queue.pop()
        
        if currNode not in visited:
            visited.add(currNode)
            
            if problem.isGoalState(currNode):
                return curr_actions
            
            for nextMove, action , stepcost in problem.getSuccessors(currNode):
                if nextMove not in visited:
                    new_cost = currCost + stepcost
                    new_action = curr_actions + [action]
                    priority_queue.push((nextMove, new_action,new_cost), new_cost) #priority is same as cost, we want the minimum cost.so we use the same parameter.
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    start = problem.getStartState() #returns the start state
    target = problem.isGoalState(start) # checking if start is a goal
    visited = {} #visited[node] = node cost
    priority_queue.push((start,[],0),0) #(state,action,cost)hueristic. cost and priority are first set to 0.
    if start == target:
        return []
    while not priority_queue.isEmpty():
        currNode, curr_actions, currCost = priority_queue.pop()
        
        if currNode in visited and visited[currNode] <= currCost : #we need to allow for revisit, in case there was another better cost
            # we can revisit the node, this lets the algorithm explore more options.
            continue
            
        visited[currNode] = currCost
        # allow revisiting for finding optimal solution.
        if problem.isGoalState(currNode):
            return curr_actions
            
        for nextMove, action , stepcost in problem.getSuccessors(currNode):
            new_cost = currCost + stepcost #g(n)
            new_action = curr_actions + [action]
            priority = new_cost + heuristic(nextMove,problem) #f(n) = g(n) + h(n)
            priority_queue.push((nextMove, new_action,new_cost), priority) 

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
