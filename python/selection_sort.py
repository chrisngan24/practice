def selectionSort(list):	
	for i in range(0,len(list)):		
		index = i
		for j in range(i, len(list)):
			if list[j] < list[index]:
				index = j
		swap(list, i, index)
		

	return list

def insertionSort(list):
	for i in range(0, len(list)-1):
		for j in range(0, i):
			if list[j] > list[j+1]:
				swap(list, j, j+1)
		

def swap(index, a, b):
	c = index[a]
	index[a] = index[b]
	index[b] = c

if __name__ == "__main__":
	list = [2,4,6,1,0,3,232]
	list = insertionSort(list)
	print str(list)