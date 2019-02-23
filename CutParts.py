from decimal import Decimal

debug = False

def main():
	y = Decimal(input("Length of buyable part: ").strip(" "))
	cont = True
	inputParts = []
	while(cont):
		temp = input('Add part length, or "end" to finish adding parts: ')
		if temp.strip(" ") == "end":
			cont = False
		elif temp.strip(" ") == "":
			pass
		else:
			inputParts.append(Decimal(temp.strip(" ")))
	buys, sets, excess = findParts(y, inputParts)
	print("buys: {}".format(buys))
	print("sets:")
	for i in range(len(sets)):
		print(sets[i])
	print("excess:")
	for i in range(len(excess)):
		print(excess[i])




# test case: max 10: 5 4 3 2
# test case: max 10: 5 5 4
# test case: max 10: 10 9 8 7 6 5 4 3 2 1
#	[10], [9,1], [8,2], [7,3], [6,4], [5]



# this should set up the recursion
def findParts(maxLength, partsList):
	partsList.sort()
	partsList.reverse()
	buys = 0
	currPartsList = partsList #not a copy
	sets = []
	excess = []
	while len(partsList) > 0:
		if debug:print("main findparts loop, buys = {}".format(buys))
		if debug:print("<==================================")
		asdf, bestSet, bestRemaining, diff = findRecursive(maxLength, [], partsList.copy())
		if debug:print("==================================>")
		excess.append(maxLength - sum(bestSet))
		sets.append(bestSet.copy())
		while len(bestSet) > 0:
			partsList.remove(bestSet.pop())
		buys += 1
	return buys, sets, excess


# for the currSet, find a part to add
# max length isn't ever changed, I'm just too lazy to create a class
def findRecursive(maxLength, currSet, currRemaining):
	if debug:
		print("========currSet:")
		print(currSet)
		print("currRemaining")
		print(currRemaining)
	if len(currRemaining) == 0:
		return maxLength, currSet, currRemaining, maxLength - sum(currSet) 
	bestSet = currSet
	bestRemaining = currRemaining
	diff = 10000 # high number
	for i in range(len(currRemaining)):
		if(sum(currSet) + currRemaining[i] > maxLength):
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
	diff = maxLength - sum(currSet)
	return maxLength, bestSet, bestRemaining, diff




if __name__ == '__main__': main()