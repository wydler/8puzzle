from Tkinter import *
import tkMessageBox
from time import sleep

from DFS import *
from BFS import *
from IDDFS import *
from AStar import *

class GUI:
    root = None
    values = []
    goal = []

    def __init__(self):
        self.root = Tk()
        self.root.bind_all('<Key>', self.keypress)
        self.values = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.update()
        self.root.mainloop()

    def keypress(self, event):
        if event.keysym == 'Left':
            self.move('Left')
        if event.keysym == 'Right':
            self.move('Right')
        if event.keysym == 'Up':
            self.move('Up')
        if event.keysym == 'Down':
            self.move('Down')

        self.update()

        s = None
        if event.char == 'b':
            print "Breitensuche"
            s = BFS({'depth' : 0, 'values' : self.values, 'parent' : None}, self.goal)
        if event.char == 'd':
            print "Tiefensuche"
            s = DFS({'depth' : 0, 'values' : self.values, 'parent' : None}, self.goal)
        if event.char == 'i':
            print "Iterative Tiefensuche"
            s = IDDFS({'depth' : 0, 'values' : self.values, 'parent' : None}, self.goal)
        if event.char == 'a':
            print "A* Suche"
            s = AStar({'depth' : 0, 'values' : self.values, 'parent' : None}, self.goal)

        if s:
            steps = []
            while s.solution['parent']:
                steps.append(s.solution['values'])
                s.solution = s.solution['parent']

            while len(steps) > 0:
                print steps.pop()

    def move(self, direction):
        i = self.values.index(0)

        if direction == 'Left':
            if i%3 != 0:
                self.values[i], self.values[i-1] = self.values[i-1], self.values[i]
                print direction

        if direction == 'Right':
            if i%3 != 2:
                self.values[i], self.values[i+1] = self.values[i+1], self.values[i]
                print direction

        if direction == 'Up':
            if i > 2:
                self.values[i], self.values[i-3] = self.values[i-3], self.values[i]
                print direction

        if direction == 'Down':
            if i < 6:
                self.values[i], self.values[i+3] = self.values[i+3], self.values[i]
                print direction

    def update(self):
        for i,v in enumerate(self.values):
            if v == '0':
                Label(self.root, text="-").grid(row=i-i%3, column=i%3, padx=10, pady=10)
            else:
                Label(self.root, text=v).grid(row=i-i%3, column=i%3, padx=10, pady=10)

        if self.values == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            tkMessageBox.showinfo("Success", "SOLVED")

GUI()
