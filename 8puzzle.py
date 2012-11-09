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

	return True

def swap(state, i, j):
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

	if event.char == 's':
		print "solve now"
		breitensuche(state, goal)

def has_adj(active):
	i = active.index('0')

	if i%3 != 0:
		return True
	elif i%3 != 2:
		return True
	elif i > 2:
		return True
	elif i < 6:
		return True
	else:
		return False

def get_adj(active):
	i = active.index('0')
	adj = []

	if i%3 != 0:
		tmp = active[:]
		adj.append(swap(tmp, i, i-1))
	if i%3 != 2:
		tmp = active[:]
		adj.append(swap(tmp, i, i+1))
	if i > 2:
		tmp = active[:]
		adj.append(swap(tmp, i, i-3))
	if i < 6:
		tmp = active[:]
		adj.append(swap(tmp, i, i+3))

	return adj

def breitensuche(state, goal):
	queue = [state]
	visited = []

	while len(queue) > 0:
		active = queue.pop(0)
		visited.append(active)

		if has_adj(active):
			for node in get_adj(active):
				if node in visited:
					continue
				if node == goal:
					print 'SOLVED!' 
					print node
					return True
				queue.append(node)

	return False


root = Tk()
root.bind_all('<Key>', keypress)

update()

root.mainloop()