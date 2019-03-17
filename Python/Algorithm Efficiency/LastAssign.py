import random	
import time

def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if alist[location]>alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp
	
def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
				
def mergeSort(alist):
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0
		j = 0
		k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k]=lefthalf[i]
				i+=1
			else:
				alist[k]=righthalf[j]
				j+=1
			k+=1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i+=1
			k+=1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j+=1
			k+=1
			
def selectdata():
	alist = []
	data = []
	listsize = []
	totaltime = 0
	size = 10000
	while totaltime < 60:
		for num in range(size):
			alist.append(random.randrange(100))	
		listsize.append(size)
		start = time.time()	
		selectionSort(alist)
		end = time.time()
		timepass = end-start
		data.append(timepass)
		size += 10000
		totaltime += timepass
	print("\n\n\tSelection Sort")
	print("List size \tExecution time (s)")
	for i in range(len(data)):
		print("%d \t\t %.5f" % (listsize[i], data[i]))
	
def bubbledata():
	alist = []
	data = []
	listsize = []
	totaltime = 0
	size = 10000
	while totaltime < 60:
		for num in range(size):
			alist.append(random.randrange(100))
		listsize.append(size)	
		start = time.time()	
		bubbleSort(alist)
		end = time.time()
		timepass = end-start
		data.append(timepass)
		size += 10000
		totaltime += timepass
	print("\n\n\tBubble Sort")
	print("List size \tExecution time (s)")
	for i in range(len(data)):
		print("%d \t\t %.5f" % (listsize[i], data[i]))

def mergedata():
	alist = []
	data = []
	listsize = []
	totaltime = 0
	size = 10000
	while totaltime < 60:
		for num in range(size):
			alist.append(random.randrange(100))	
		listsize.append(size)
		start = time.time()	
		mergeSort(alist)
		end = time.time()
		timepass = end-start
		data.append(timepass)
		size += 10000
		totaltime += timepass
	print("\n\n\tMerge Sort")
	print("List size \tExecution time (s)")
	for i in range(len(data)):
		print("%d \t\t %.5f" % (listsize[i], data[i])) 
	
def main():
	mergedata()
	bubbledata()
	selectdata()
	
if __name__ == "__main__":
	main()