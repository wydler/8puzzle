from Tkinter import *

state = ['1', '3', '0', '5', '2', '6', '4', '7', '8']
goal = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
moves = 0

def update():
	for i,v in enumerate(state):
		if v == '0':
			Label(root, text="-").grid(row=i-i%3, column=i%3, padx=10, pady=10)
		else:
			Label(root, text=v).grid(row=i-i%3, column=i%3, padx=10, pady=10)

def move(direction):
	i = state.index('0')

	if direction == 'Left':
		if i%3 != 0:
			swap(i, i-1)
		else:
			return False

	if direction == 'Right':
		if i%3 != 2:
			swap(i, i+1)
		else:
			return False

	if direction == 'Up':
		if i > 2:
			swap(i, i-3)
		else:
			return False

	if direction == 'Down':
		if i < 6:
			swap(i, i+3)
		else:
			return False

	update()
	if is_done():
		print "SOLVED!"
	return True

def swap(i, j):
	state[i], state[j] = state[j], state[i]
	return state

def is_done():
	if state == goal:
		return True

def keypress(event):	
	if event.keysym == 'Left':
		move('Left')
	if event.keysym == 'Right':
		move('Right')
	if event.keysym == 'Up':
		move('Up')
	if event.keysym == 'Down':
		move('Down')

	if event.char == 'b':
		print "Breitensuche"
		BFS(state).start()
	if event.char == 'd':
		print "Tiefensuche"
		DFS(state).start()

class DFS:
	state = []

	def __init__(self, state):
		self.state = state

	def start(self):
		if self.state == goal:
			print self.state
			return self.state
		else:
			nodes = self.nodes(self.state)
			for node in nodes:
				return DFS(node).start()	

	def nodes(self, current):
		i = current.index('0')
		nodes = []

		if i%3 != 0:
			tmp = current[:]
			tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
			nodes.append(tmp)
		if i%3 != 2:
			tmp = current[:]
			tmp[i], tmp[i-1] = tmp[i-1], tmp[i]
			nodes.append(tmp)
		if i > 2:
			tmp = current[:]
			tmp[i], tmp[i-3] = tmp[i-3], tmp[i]
			nodes.append(tmp)
		if i < 6:
			tmp = current[:]
			tmp[i], tmp[i+3] = tmp[i+3], tmp[i]
			nodes.append(tmp)

		return nodes

class BFS:
	queue = []
	visited = []

	def __init__(self, state):
		self.queue.append(state)

	def start(self):
		while len(self.queue) > 0:
			active = self.queue.pop(0)
			self.visited.append(active)

			nodes = self.nodes(active)
			if len(nodes) > 0:
				for node in nodes:
					if node in self.visited:
						continue
					if node == goal:
						print 'SOLVED!' 
						print node
						return True
					self.queue.append(node)

		return False

	def nodes(self, current):
		i = current.index('0')
		nodes = []

		if i%3 != 0:
			tmp = current[:]
			tmp[i], tmp[i-1] = tmp[i-1], tmp[i]
			nodes.append(tmp)
		if i%3 != 2:
			tmp = current[:]
			tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
			nodes.append(tmp)
		if i > 2:
			tmp = current[:]
			tmp[i], tmp[i-3] = tmp[i-3], tmp[i]
			nodes.append(tmp)
		if i < 6:
			tmp = current[:]
			tmp[i], tmp[i+3] = tmp[i+3], tmp[i]
			nodes.append(tmp)

		return nodes


root = Tk()
root.bind_all('<Key>', keypress)

update()

root.mainloop()