import random 
from copy import deepcopy 

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


if __name__ == "__main__":
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
			break
	print map