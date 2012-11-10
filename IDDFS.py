from Shared import *

class IDDFS:
    solution = None
    
    def __init__(self, state, goal):
        depth = 0
        solution = None

        while not solution:
            solution = self.dls(state, goal, depth)
            depth = depth + 1

    def dls(self, state, goal, depth):
        if state['values'] == goal:
            print 'SOLVED!'
            self.solution = state
            return state

        for node in expand(state):
            if node['depth'] < depth:
                result = self.dls(node, goal, depth);
                if result:
                    return result

        return None
