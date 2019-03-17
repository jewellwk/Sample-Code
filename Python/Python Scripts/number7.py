#Number 1
"""The revString method returns the reverse of a String that it accepts as a parameter denoted as 'letters'"""
def revString(letters):
	#base case
	if (len(letters) == 1):
		return letters
	else:	
		#change of state - moves first char to the end of the String and decrements the beginning until the base case is reached. 
		return revString(letters[1:]) + letters[0]
		
#Number 2
"""The recString method formats a String by printing each char from the end of the String until the base case is reached."""
def recString(letters):
	if recString.count == 0:
		print('*')
	else:
		i = len(letters) - recString.count
		#while loop that prints each letter on a single line starting with the last char
		while i <len(letters):
			print(letters[i], end='')
			i+=1
		print('') #line break
	#base case - once the count has accounted for every letter then recursion ceases
	if recString.count == len(letters):
		return ''
	#change of state - by incrementing the count, it iterates over each char
	recString.count +=1
	#actual String value is never changed or else this doesn't work
	recString(letters)
recString.count = 0	

def recStringRight(letters):
	if len(letters) == 0:
		print('*')
	else:
		recStringRight(letters[1:])
		print(letters)
	
"""The h method is the hash function for numbers 3 and 4 of the assignment."""	
def h(i):
	return (2*i+5)%11

					
def main():
	print(revString('stressed')) #stressed spelled backwards is desserts
	recString('abcde')
	print(h(38))
	recStringRight('abcde')
	
if __name__== "__main__":
	main()