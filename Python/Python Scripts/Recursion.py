#recursion functions like while loops 
#recursions must have a base case, must change its state and move towards the base case and must call itself recursively
from functools import lru_cache
def countdown(n):
	if n == 0:
		print(n)
	else:
		print(n)
		countdown(n-1)

def backwardsAlphabet(letter):
	if (letter == 'a'):
		print(letter)
	else:
		print(letter)
		letterprev = chr(ord(letter)-1)
		backwardsAlphabet(letterprev)

@lru_cache(maxsize=1000)
def factorial(n):
	if n == 0 :
		return 1
	else:
		return n * factorial(n-1) 
		
def fibonacci(n):
#	x^n = x^n+1 + x^n+2
	if (n == 0):
		return 0
	elif (n == 1 or n == 2):
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	
def palindrome(s):
	if len(s) <= 1:
		return True
	elif s[0] != s[-1]:
		return False
	else:
		return palindrome(s[1:-1])
		
def checklist(alist):
	if len(alist) == 0:
		return ""
	else:
		checklist(alist[1:])
		print(alist[0])
				
def checkn(n):
	if n < 0:
		return 2
	else:
		return 2 * checkn(n-2)
		
def recString(letters):
	if len(letters) == 0:
		print('*')
	else:
		recString(letters[1:])
		print(letters)
		
#rec(5) --> 2 * rec(3)
#2 * rec(1)
#2 * rec(-1)
#2
#Substitute the value after the base case ceases. Then go back and reevaluate. 
#Then it becomes 2 * 2 = 4
#4 * 2 = 8
#8 * 2 = 16
					
def main():
	countdown(4)
	backwardsAlphabet('c')
	print(fibonacci(5))
	print(factorial(4))
	print(palindrome("mom"))
	checklist([5,4,3,2,1])
	print(checkn(5))
	recString('abcde')

if __name__ == "__main__":
	main()