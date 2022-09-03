import itertools
import random
def feasWord(split, grid):
	## returns whether or not all chars in word are in the grid
	for char in split:
		## also check to see if there is enough of that char because you can't repeat
		if char not in grid or split.count(char) > grid.count(char): 
			return False
	return True

def getNeighbors():
	neighbors = []
	## get neighbors of every cell
	for x in range(4):
		t = []
		for y in range(4):
			temp = []
			for x2 in range(x-1,x+2):
				for y2 in range(y-1,y+2):
					if (-1 < x < 4 and -1 < y < 4 and (x != x2 or y != y2) and (0 <= x2 < 4) and (0 <= y2 < 4)):
						temp.append((x2,y2))
			t.append(temp)
		neighbors.append(t)
	return neighbors

## check if word is connecting in the grid
def connecting(word,grid,neighbors):
	together = [i for x in grid for i in x] ## grid as 1d array
	split = map(str,word) ## split word
	coords = []
	n = []

	for i in range(len(word)):
		temp = []
		for x in range(4):
			for y in range(4):
				if grid[x][y] == word[i]:
						temp.append((x,y))
				
		coords.append(temp)


	paths = []
	

	combos = (list(itertools.product(*coords))) 
	counts = []


	for j in range(len(combos)):
		t = []
		c = 0
		
		if sorted(list(set(combos[j]))) == sorted(combos[j]):
			for i in range(1, len(combos[j])):
				x = combos[j][i][0]
				y = combos[j][i][1] 
				cord = combos[j][i]
				temp = neighbors[x][y]
				#print combos[j][i], temp
				if combos[j][i-1] in temp:
					c += 1

				t.append(temp)
			counts.append(c)
			n.append(t)
			#print

	#print counts
	if any(x == len(word)-1 for x in counts):
		return True
	return False

	

def solve(grid):
	neighbors = getNeighbors()
	words = open("words.txt","r")
	words = [x.replace("\n","") for x in words.readlines()]
	gridTogether = [i for x in grid for i in x]
	feas = []
	
	## make feasible set of words
	for word in words:
		split = map(str,word)
		if feasWord(split, gridTogether):
			feas.append(word)

	final = []

	
	## goes through feasible words and checks which ones are connecting
	for word in feas:
		if connecting(word, grid,neighbors) and len(word) > 2:
			final.append(word)
	
	return final
	

	
"""
## SORT DATABASE BY LENGTH OF WORD
read = open("words.txt","r")
read = [x.replace("\n","") for x in read.readlines()]

read = sorted(read, key = lambda p: len(p))
with open("sorted.txt","w") as out:
	for item in read:
		#print item
		out.write(item+"\n")
"""

infile = open("input.txt","r")
grid = []
for i in range(4):
	grid.append(infile.readline().strip().lower().split())


sol = solve(grid)
write = ""
writeLong = ""



size = random.randint(63,70) ##how many answers you want to get
size = 68
ind = range(size+1)
random.shuffle(ind)
random.shuffle(sol)

for x in range(size):
	write += sol[ind[x]]+"\n"


for x in sol:
	writeLong += x+"\n"

print write
print len(write.split())


with open("shortsolution.txt","w") as out:
	out.write(str(write))
	out.write(str(len(write.split())))

with open("longsolution.txt","w") as out:
	out.write(str(writeLong))
	out.write(str(len(writeLong.split())))
