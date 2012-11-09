import copy
from Tkinter import *

state = {"depth" : 0, "values" : ['1', '3', '0', '5', '2', '6', '4', '7', '8'], "parent" : None}
goal = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
moves = 0

def update(state):
	for i,v in enumerate(state):
		if v == '0':
			Label(root, text="-").grid(row=i-i%3, column=i%3, padx=10, pady=10)
		else:
			Label(root, text=v).grid(row=i-i%3, column=i%3, padx=10, pady=10)

def move(state, direction):
	i = state.index('0')

	if direction == 'Left':
		if i%3 != 0:
			swap(state, i, i-1)
		else:
			return False

	if direction == 'Right':
		if i%3 != 2:
			swap(state, i, i+1)
		else:
			return False

	if direction == 'Up':
		if i > 2:
			swap(state, i, i-3)
		else:
			return False

	if direction == 'Down':
		if i < 6:
			swap(state, i, i+3)
		else:
			return False

	update(state)
	if is_done(state):
		print "SOLVED!"
	return True

def swap(state, i, j):
	state[i], state[j] = state[j], state[i]
	return state

def is_done(state):
	if state == goal:
		return True

def keypress(event):	
	if event.keysym == 'Left':
		move(state['values'], 'Left')
	if event.keysym == 'Right':
		move(state['values'],'Right')
	if event.keysym == 'Up':
		move(state['values'],'Up')
	if event.keysym == 'Down':
		move(state['values'],'Down')

	if event.char == 'b':
		print "Breitensuche"
		BFS().solve(state)
	if event.char == 'd':
		print "Tiefensuche"
		DFS().solve(state)
	if event.char == 'i':
		print "Iterative Tiefensuche"
		IDDFS().solve(state)

class DFS:
	def solve(self, state):
		if state == goal:
			print 'SOLVED!'
			print state
			return state

		for node in expand(state):
			return DFS().solve(node)

class BFS:
	queue = []
	visited = []

	def solve(self, state):
		self.queue = [state]
		self.visited = []

		while len(self.queue) > 0:
			active = self.queue.pop(0)
			self.visited.append(active['values'])

			nodes = expand(active)
			if len(nodes) > 0:
				for node in nodes:
					if node['values'] in self.visited:
						continue
					if node['values'] == goal:
						print 'SOLVED!'
						print node
						return True
					self.queue.append(node)

		return False

class IDDFS:
	def solve(self, node):
		depth = 0
		solution = None

		while not solution:
			solution = DLS().solve(node, depth)
			depth = depth + 1

		return solution
			
class DLS:
	def solve(self, state, depth):
		#print state
		if state['values'] == goal:
			print "SOLVED \n" + str(state)
			return state

		for node in expand(state):
			if node['depth'] < depth:
				result = DLS().solve(node, depth);
				if result:
					return result

		return None

def expand(node):
	i = node['values'].index('0')
	nodes = []

	if i%3 != 0:
		tmp = copy.deepcopy(node)
		tmp['depth'] = node['depth'] + 1
		tmp['values'][i], tmp['values'][i-1] = tmp['values'][i-1], tmp['values'][i]
		tmp['parent'] = node
		nodes.append(tmp)
	if i%3 != 2:
		tmp = copy.deepcopy(node)
		tmp['depth'] = node['depth'] + 1
		tmp['values'][i], tmp['values'][i+1] = tmp['values'][i+1], tmp['values'][i]
		tmp['parent'] = node
		nodes.append(tmp)
	if i > 2:
		tmp = copy.deepcopy(node)
		tmp['depth'] = node['depth'] + 1
		tmp['values'][i], tmp['values'][i-3] = tmp['values'][i-3], tmp['values'][i]
		tmp['parent'] = node
		nodes.append(tmp)
	if i < 6:
		tmp = copy.deepcopy(node)
		tmp['depth'] = node['depth'] + 1
		tmp['values'][i], tmp['values'][i+3] = tmp['values'][i+3], tmp['values'][i]
		tmp['parent'] = node
		nodes.append(tmp)

	return nodes

root = Tk()
root.bind_all('<Key>', keypress)

update(state['values'])

root.mainloop()