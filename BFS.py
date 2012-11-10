from Shared import *

class BFS:
    solution = None

    def __init__(self, state, goal):
        queue = [state]
        visited = []

        while len(queue) > 0:
            active = queue.pop(0)
            visited.append(active['values'])

            nodes = expand(active)
            if len(nodes) > 0:
                for node in nodes:
                    if node['values'] in visited:
                        continue
                    
                    if node['values'] == goal:
                        print 'SOLVED!'
                        self.solution = node
                        return

                    queue.append(node)
