from Shared import *

class DFS:
    solution = None
    
    def __init__(self, state, goal):
        if state == goal:
            print 'SOLVED!'
            self.solution = state
            return

        for node in expand(state):
            DFS(node, goal)
