import Tkinter as tk
from time import sleep
import math
import random 
from copy import deepcopy 

def update(window , map):
	context = [[0 for i in range(4)]for j in range(4)]
	color = ['#EEE4DA', '#eee4da', '#ede0c8', '#f2b179',
		'#f59563', '#f67c5f', '#f65e3b', '#edcf72',
		'#edcc61', '#edc850', '#edc53f', '#edc22e']
	for i in range(4):
		for j in range(4):
			ci = 0
			if(map[i][j]==0): ci =0 
			else:	ci=math.log(map[i][j],2)
			k = tk.Label(window,
				text = map[i][j], bg = color[int(ci)],
				font=('Arial', 24), width = 4, height = 2
			)
			context[i][j] = k
			context[i][j].grid(column=j, row=i, padx=5, pady=5)
	window.update_idletasks()

#==============================
def makeblock(map):
	number = [ 2, 4 ]
	newblock = number[random.randint(0,1)]
	print newblock
	while True:
		x, y = random.randint(0, 3),random.randint(0, 3)
		if(map[x][y]==0): 
			map[x][y] = newblock
			break

def movemap(map, dir):
	dirmap = {
		'left': dorowfun,
		'top': docolfun,
		'down': docolfun,
		'right': dorowfun,
	}
	dirmap.get(dir)(map, dir)

# accord row move left and right
def dorowfun(map, dir):
	checkmap = [[0 for i in range(4)]for j in range(4)]
	for x in range(4):
		rowmove(map, x, dir)
		checkmap = deepcopy(map)
		rowadd(map, x, dir)
	while(checkmap != map):
		for x in range(4):
			rowmove(map, x, dir)
			checkmap = deepcopy(map)
			rowadd(map, x, dir)

def rowadd(map, x, dir ):
	if(dir == 'left'):
		for dy in range(3):
			if(map[x][dy] == map[x][dy+1]):
				map[x][dy] += map[x][dy]
				map[x][dy+1] = 0
	elif(dir=='right'):
		for dy in range(3, 0, -1):
			if(map[x][dy] == map[x][dy-1]):
				map[x][dy] += map[x][dy]
				map[x][dy-1] = 0

def rowmove(map, x, dir ):
	if(dir == 'left'):
		for move in range(4):
			for dy in range(1,4):
				if(map[x][dy-1]==0 and map[x][dy]!=0 ):
					map[x][dy-1] = map[x][dy]
					map[x][dy] = 0
	elif(dir=='right'):
		for move in range(4):
			for dy in range(0,3):
				if(map[x][dy+1]==0 and map[x][dy]!=0 ):
					map[x][dy+1] = map[x][dy]
					map[x][dy] = 0

# accord col move top and down.
def docolfun(map, dir):
	checkmap = [[0 for i in range(4)]for j in range(4)]
	for y in range(4):
		colmove(map, y, dir)
		checkmap = deepcopy(map)
		coladd(map, y, dir)
	while(checkmap != map):
		for y in range(4):
			colmove(map, y, dir)
			checkmap = deepcopy(map)
			coladd(map, y, dir)

def coladd(map, y, dir ):
	if(dir == 'top'):
		for dx in range(3):
			if(map[dx][y] == map[dx+1][y]):
				map[dx][y] += map[dx][y]
				map[dx+1][y] = 0
	elif(dir=='down'):
		for dx in range(3, 0, -1):
			if(map[dx][y] == map[dx-1][y]):
				map[dx][y] += map[dx][y]
				map[dx-1][y] = 0

def colmove(map, y, dir ):
	if(dir == 'top'):
		for move in range(4):
			for dx in range(1,4):
				if(map[dx-1][y]==0 and map[dx][y]!=0 ):
					map[dx-1][y] = map[dx][y]
					map[dx][y] = 0
	elif(dir=='down'):
		for move in range(4):
			for dx in range(0,3):
				if(map[dx+1][y]==0 and map[dx][y]!=0 ):
					map[dx+1][y] = map[dx][y]
					map[dx][y] = 0

def deaddetected(map):
	count = 0
	action = [ 'left', 'top', 'down', 'right' ]
	dirmap = {
		'left': dorowfun,
		'top': docolfun,
		'down': docolfun,
		'right': dorowfun,
	}
	for i in range(4):
		deadmap = deepcopy(map)
		dirmap.get(action[i])(deadmap,action[i])
		if(deadmap == map): count+=1
	if(count==4): return 1
	else: return 0

if __name__ ==  '__main__':
	window = tk.Tk()
	window.title('2048')
	window.geometry('350x350')
	color = ['#EEE4DA', '#eee4da', '#ede0c8', '#f2b179',
			'#f59563', '#f67c5f', '#f65e3b', '#edcf72',
			'#edcc61', '#edc850', '#edc53f', '#edc22e']
	map = [[0 for i in range(4)]for j in range(4)]
	oldmap = [[0 for i in range(4)]for j in range(4)]
	oldmap = deepcopy(map)
	dirmap = {
		'A': 'left', 'a': 'left',
		'W': 'top',	'w': 'top',
		'S': 'down', 's': 'down',
		'D': 'right', 'd': 'right',
		'B': 'back', 'b': 'back'
	}
	makeblock(map)
	while True:
		for i in map : print i
		update(window,map)
		dir = raw_input('input char A W S D or back.\n')
		dir = dirmap[dir]
		if(dir == 'back'):
			map = deepcopy(oldmap)
			makeblock(map)
			continue
		oldmap = deepcopy(map)
		movemap(map, dir)
		if(oldmap != map): makeblock(map)
		if(deaddetected(map)): 
			print 'dead'
			for i in map : print i
			update(window,map)
			break
	print map



