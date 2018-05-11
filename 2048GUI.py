import Tkinter as tk
import tkMessageBox as tkmesg
from time import sleep
import math
import random 
from copy import deepcopy 
import threading

# mainloop_started = threading.Event()
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

def update(window , map): 
	color = ['#EEE4DA', '#eee4da', '#ede0c8', '#f2b179',
		'#f59563', '#f67c5f', '#f65e3b', '#edcf72',
		'#edcc61', '#edc850', '#edc53f', '#edc22e']
	tolog ={
		"0": 0, "2": 1, "4": 2, "8": 3, "16": 4,
		"32": 5, "64": 6, "128": 7, "256": 8,
		"512": 9, "1024": 10, "2048": 11,
	}
	for i in range(4):
		for j in range(4):
			tk.Label(window, text = map[i][j], bg = color[ tolog[ str(map[i][j]) ] ],
				font=('Arial', 24), width = 4, height = 2
			).grid(column=j, row=i, padx=5, pady=5)
	window.update_idletasks()

#==============================
def makeblock(map):
	number = [ 2, 4 ]
	newblock = number[random.randint(0,1)]
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

def findmax(map):
	max =0
	for i in range(4):
		for j in range(4):
			if(max < int(map[i][j]) ): max = int(map[i][j]) 
	return max

def getscore(map):
	max =0
	for i in range(4):
		for j in range(4):
			if(max < int(map[i][j]) ): max = int(map[i][j]) 
	score = 0 
	if( max >=2048): score = 40
	elif( max >= 1024 ): score = 30
	elif( max >= 512 ): score = 20
	elif( max >= 256 ): score = 10
	elif( max >= 128 ): score = 5
	return score

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

def printkey(event):
	global map, oldmap, dirmap
	dir = dirmap[event.char]
	if(dir == 'back'):
		map = deepcopy(oldmap)
		makeblock(map)
		update(window,map)
		return 
	oldmap = deepcopy(map)
	movemap(map, dir)
	if(oldmap != map): makeblock(map)
	if(deaddetected(map)): 
		print 'dead'
		for i in map : print i
		update(window,map)
		score = getscore(map)
		token = tkmesg.askokcancel("Game Over", "your score is " + str(score) + "\nClose window click \'OK\'")
		if token:
			window.quit()
		return 
	update(window,map)

def ai():
	global map, oldmap, dirmap
	makeblock(map)
	update(window,map)
	movedir=1
	downfilure=0
	ltlaw = ['a', 'w']
	lttoken = [0, 0]
	while True:
		# sleep(0.5)
		lawact = lttoken[0] + lttoken[1]
		if(lawact<2): dir = dirmap[ltlaw[movedir]]
		elif(downfilure): 
			downfilure = 0
			dir = dirmap['d']
		else: dir = dirmap['s']
		print dir
		oldmap = deepcopy(map)
		movemap(map, dir)
		if(movedir==0):movedir=1
		elif(movedir==1):movedir=0
		if(oldmap != map): 
			lttoken[0]=0
			lttoken[1]=0
			makeblock(map)
			if(((dir=='down' or dir=='right') and map[0]==[0,0,0,0]) or findmax(map) in map[0]): movedir=0
			elif((dir=='down' or dir=='right') and map[0]!=[0,0,0,0]): movedir=1
		else: 
			if(dir=='right'): downfilure=1
			lttoken[movedir]=1

		if(deaddetected(map)): 
			print 'dead'
			for i in map : print i
			update(window,map)
			score = getscore(map)
			token = tkmesg.askokcancel("Game Over", "your score is " + str(score) + "\nClose window click \'OK\'")
			if token:
				window.quit()
			return 
		update(window,map)

def user():
	global map
	window.bind('<Key>', printkey)
	makeblock(map)
	update(window,map)


if __name__ ==  '__main__':
	window = tk.Tk()
	window.title('2048')
	window.geometry('350x350')

	B1 = tk.Button(window, text = "ai play", command = ai)
	B1.grid(column=0, row=0)
	B2 = tk.Button(window, text = "user play", command = user)
	B2.grid(column=1, row=0)


	# window.after(1000, mainloop_started.set)
	window.mainloop()
	print "END GAME"