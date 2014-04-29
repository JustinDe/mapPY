import random

y = 16
x = 8
map = []
bound = []
rooms = []
def mainFunctions():
	emptyMap()
	findBound()
	applyBound()
	buildRooms()
	applyRooms()
	printMap()

def emptyMap():
	for i in range(0,x*y):
		map.append("0")
       
def printMap():
    for i in range(0,x*y):
        if i%y == 0 and i != 0:
            print "\n"
        print map[i],

def findBound():
	for i in range(0,y):
		bound.append(i)
	for o in range(1,x+1):
		bound.append(y*o)
		bound.append((y*o)-1)
	for p in range((x*y)-y, x*y):
		bound.append(p)

def applyBound():
	for i in range(0, len(map)):
		for o in range(0, len(bound)-1):
			if i == bound[o]:
				map[i] = "X"

def buildRooms():
	#rooms are defind as a minimum of 4 spaces and a maximum of y/2 and will always be even(may change later)
	numRooms = random.randrange(1,(y/4))
	for i in range(0,numRooms):
		rmSize = random.randrange(4,y/2,2)
		#print "Room "+ str(i) +"/"+ str(numRooms-1) + " Size: "+ str(rmSize)
		rmLoc = random.randrange(0,len(map))
		for o in range(0,rmSize):
			rooms.append(rmLoc)
			rmLoc += 1
	#print rooms

def applyRooms():
	for i in range(0, len(map)):
		for o in range(0, len(rooms)):
			if i == rooms[o]:
				map[i] = "1"


mainFunctions()