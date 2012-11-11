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
                    node['score'] = self.cost_h2(node['values'])

                    if not node in queue:
                        queue.append(node)

    def cost_h1(self, node):
        cost = 0

        for i, v in enumerate(node):
            if v != 0:
                if i+1 != v:
                    cost = cost + 1

        return cost

    def cost_h2(self, node):
        cost = 0

        for i, v in enumerate(node):
            if v != 0:
                x_1 = i % 3
                y_1 = i // 3

                x_2 = v % 3
                y_2 = v // 3

                d_x = abs(x_1 - x_2)
                d_y = abs(y_1 - y_2)

                cost = cost + d_x + d_y

        return cost