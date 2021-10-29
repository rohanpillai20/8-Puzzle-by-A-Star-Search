import numpy as np
import copy
from operator import itemgetter
import sys

class Puzzle8Solver:
    def __init__(self, heuristicChoice, origin, current, ):
        self.origin = origin
        self.current = current
        self.heuristicChoice = heuristicChoice
        self.g = 0
        self.indexE = []
        for i in range(3):
            for j in range(3):
                self.indexE.append([i,j])
        self.positions = {}
        self.positions[0] = [[0,1],[1,0]]
        self.positions[1] = [[0,0],[1,1],[0,2]]
        self.positions[2] = [[0,1],[1,2]]
        self.positions[3] = [[0,0],[1,1],[2,0]]
        self.positions[4] = [[0,1],[1,0],[1,2],[2,1]]
        self.positions[5] = [[0,2],[1,1],[2,2]]
        self.positions[6] = [[1,0],[2,1]]
        self.positions[7] = [[2,0],[1,1],[2,2]]
        self.positions[8] = [[2,1],[1,2]]

    def get_manhattan(self, grid, element):
        x = np.argwhere(origin==element)
        y = np.argwhere(grid==element)
        manhattan = 0
        for i in range(2):
            manhattan+=np.abs(x[0][i]-y[0][i])
        return manhattan

    def heuristic(self, grid):
        heuristic = 0
        for i in range(1,8):
            heuristic+= self.get_manhattan(grid,i)
        return heuristic

    def printArr(self, array):
        for i in array:
            for j in i:
                if(j==0):
                    print("_", end=" ")
                else:
                    print(j, end=" ")
            print()
	
	def draw_tile(map, position, kwargs):

		# Get the map value
		value = map.get(position)
		# Check if we should print the path
		if 'path' in kwargs and position in kwargs['path']: value = '+'
		# Check if we should print start point
		if 'start' in kwargs and position == kwargs['start']: value = '@'
		# Check if we should print the goal point
		if 'goal' in kwargs and position == kwargs['goal']: value = '$'
		# Return a tile value
		return value 

    def solve(self):
        self.printArr(self.current)
        print("="*20)
        temp = self.current
        states = []
       
        ans = 0
        iter = 1
        while True:
			if(iter==20):
				break
            moves = self.positions[self.indexE.index(list(np.argwhere(temp==0)[0]))]
            currentZero = np.argwhere(temp==0)[0]
            states = []
            for i in moves:
                temp2 = copy.deepcopy(temp)
                val = temp2[i[0]][i[1]]
                temp2[currentZero[0]][currentZero[1]] = val
                temp2[i[0]][i[1]] = 0
                h = self.heuristic(temp2)
                if(h==0):
                    print("ANSWER")
                    self.printArr(temp2)
                    ans = 1
                    break
                f = iter + h
                states.append([temp2, iter, h, f])
            if(ans==1):
                break
            
            result = min(states,key=itemgetter(3))
            self.printArr(result[0])
            temp = result[0]
            print("="*20)
            iter+=1

if __name__ == "__main__":	
	origin = np.array([[0,1,2],[3,4,5],[6,7,8]])
	
	if(len(sys.argv) != 11):
		print("Enter right amount of arguments.")
		print("python Puzzle8Solver.py <heuristicChoice> <1 to 8 in any order with a _ in middle>")
		print("Example: python Puzzle8Solver.py 1 1 4 2 6 3 5 _ 7 8")
		sys.exit()
	else:
		heuristicChoice = sys.argv[1]
		curr = sys.argv[2:]
		if(sorted(curr)!=["1","2","3","4","5","6","7","8","_"]):
			print("Input all unqiue numbers from 1 to 8 in any order with a _ in between.")
		else:
			current = []
			temp = []
			count = 0
			for i in curr:
				if(count==3):
					count = 0
					current.append(temp)
					temp = []				
				if(i == "_"):
					temp.append(0)
				else:
					temp.append(int(i))
				count+=1
				
			current.append(temp)
			current = np.array(current)
			#print(current)
			obj = Puzzle8Solver(heuristicChoice, origin, current)
			obj.solve()
