#Algorithm efficiency 
#For each of the following functions code, calculate T(n), the time it takes to solve a problem of size n, and find the corresponding Big-O running time:
	
#a)	Sequential search
check = [5,1,2,4,0]

def sequentialSearch(alist, item):
	"""This is a sequential search meaning this loop will always run n number of times, which represents a linear relationship between k and n."""
	pos = 0 #1 costant 
	found = False #2 constant
	while pos <len(alist) and not found: #3 evaluation dependent n
		if alist[pos] == item: #4 evaluation dependent on n
			found = True 
		else: #5 statement dependent on n
			pos = pos +1 
	return found #6 constant
#f(n)= 3n + 3
#O(f(n))=n

#b)	Bubble sort
def bubbleSort(alist):
	"""This method has two loops. The first loop decrements n by 1 and then the second conducts 4 statements n number of times (4n). The second loop will execute n-1 number of times, which represents a quadratic relationship between k and n."""
	for passnum in range(len(alist)-1,0,-1): #modifies n
		for i in range(passnum): #dependent on modified n
			if alist[i]>alist[i+1]: #evaluation dependent on modified n
				temp = alist[i] #statement 
				alist[i] = alist[i+1] #statement
				alist[i+1] = temp #statement
	return alist #constant 
#f(n)= (n-1)*(4n) + 1
#f(n)= 4n^2-4n + 1
#O(f(n))=n^2
	
#c)	Binary search
def binarySearch (alist, item):
	"""This is supposed to be a method conducting a binary search. However it doesn't check the odd indexes. Therefore it's not executing correctly. A binary search should divide n by 2 and then sequentially search through the first set and then the second set if it doesn't find what it's looking for. Best case scenario, it executes once and finds the item in the first set (log n). Worst case scenario it goes through both sets and doesn't find what it's looking for (linear n)."""
	first=0 #constant
	last=len(alist)-1 #constant dependent on n
	found=False #constant
	while first<=last and not found: #evaluation
		midpoint=(first+last)/2 #statement 
		if alist[int(midpoint)] == item: #evaluation
			found = True 
		else: #statement 
			if item<alist[int(midpoint)]: 
				last=midpoint-1 
			else: #statement
				first=midpoint+1
	return found #constant
#f(n)= 5log(n)+4 > 2
#O(f(n))= log(n)

def main():
	print(sequentialSearch(check,11))
	print(bubbleSort(check))
	print(binarySearch(check,1))
			
if __name__ == "__main__":
	main()  


