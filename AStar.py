from Shared import *
from operator import itemgetter

class AStar:
    solution = None
    
    def __init__(self, state, goal):
        queue = [state]
        visited = []

        state['score'] = self.cost_h1(state['values'])

        while len(queue) > 0:
            queue = sorted(queue, key=itemgetter('score')) 
            current = queue.pop(0)
            visited.append(current['values'])

            if current['values'] == goal:
                self.solution = current
                return

            for node in expand(current):
                if node['values'] in visited:
                    continue

                if not node['values'] in visited:
                    node['score'] = self.cost_h1(node['values'])

                    if not node in queue:
                        queue.append(node)

    def cost_h1(self, node):
        cost = 0

        if node[0] != '1':
            cost = cost + 1
        if node[1] != '2':
            cost = cost + 1
        if node[2] != '3':
            cost = cost + 1
        if node[3] != '4':
            cost = cost + 1
        if node[4] != '5':
            cost = cost + 1
        if node[5] != '6':
            cost = cost + 1
        if node[6] != '7':
            cost = cost + 1
        if node[7] != '8':
            cost = cost + 1
        if node[8] != '0':
            cost = cost + 1

        return cost