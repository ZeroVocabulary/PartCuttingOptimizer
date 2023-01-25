from decimal import Decimal
import numpy as np
debug = False
class Cut:
	CutNumber:int
	CutSize:int
	def __init__(self,cutNumber:int,cutSize:int):
		self.CutNumber=cutNumber
		self.CutSize=cutSize

def main():
	y = 5600
	cuts=[Cut(1,2256),Cut(1,2256),Cut(1,963),Cut(1,963),
	Cut(2,1846),Cut(2,1846),Cut(2,936),Cut(2,936)
	]
	buys, sets, excess = findParts(y, cuts)
	print("buys: {}".format(buys))
	print("sets:")

	templist=[]
	tt=[]
	
	for i in range(len(sets)):
		tt=[]
		for cut in sets[i]:
			tt.append("({0},{1})".format(cut.CutNumber,cut.CutSize))
		templist.append(tt)
	for i in templist:
		print(i)
		#print(sets[i],np.sum(sets[i]))
        

	print("excess:")
	for i in range(len(excess)):
		print(excess[i])



# this should set up the recursion
def findParts(maxLength:int, partsList:list[Cut]):
	partsList.sort(key=lambda x: x.CutSize, reverse=True)
	#partsList.reverse() #already reversed

	buys = 0
	currPartsList = partsList #not a copy
	sets = []
	excess = []
	while len(partsList) > 0:
		if debug:print("main findparts loop, buys = {}".format(buys))
		if debug:print("<==================================")
		asdf, bestSet, bestRemaining, diff = findRecursive(maxLength, [], partsList.copy())
		if debug:print("==================================>")
		excess.append(maxLength - sum(x.CutSize for x in  bestSet))
		sets.append(bestSet.copy())
		while len(bestSet) > 0:
			partsList.remove(bestSet.pop())
		buys += 1
	return buys, sets, excess


# for the currSet, find a part to add
def findRecursive(maxLength, currSet:list[Cut], currRemaining:list[Cut]):
	if debug:
		print("========currSet:")
		print(currSet)
		print("currRemaining")
		print(currRemaining)
	if len(currRemaining) == 0:
		return maxLength, currSet, currRemaining, maxLength - sum(x.CutSize for x in  currSet) 
	bestSet = currSet
	bestRemaining = currRemaining
	diff = 10000 # high number
	for i in range(len(currRemaining)):
		if(sum(x.CutSize for x in currSet) + currRemaining[i].CutSize > maxLength):
			pass
		else:
			currSet2 = currSet.copy()
			currRemaining2 = currRemaining.copy()
			currSet2.append(currRemaining2[i])
			currRemaining2 = currRemaining[i+1:]
			asdf, currSet3, currRemaining3, diffNew = findRecursive(maxLength, currSet2, currRemaining2)
			if diffNew < diff:
				bestSet = currSet3
				bestRemaining = currRemaining3
				diff = diffNew
			if debug:
				print("checking diff == 0: {}".format(diff))
			if diff == 0:
				if debug:
					print("diff is equal to 0")
				return maxLength, bestSet, bestRemaining, diff
	diff = maxLength - sum(x.CutSize for x in currSet)
	return maxLength, bestSet, bestRemaining, diff




if __name__ == '__main__': main()
