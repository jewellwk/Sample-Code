#Compute the Cartesian distance between 2 points with coordinates (x1,y1) and (x2,y2) = sqrt((x2-x1)^2+(y2-y1)^2))
import math
def solveCart():
	x1 = int(input("Enter a value for x1: "))
	y1 = int(input("Enter a value for y1: "))
	x2 = int(input("Enter a vlaue for x2: "))
	y2 = int(input("Enter a value for y2: "))

	cart = math.sqrt((x2-x1)**2 + (y2-y1)**2)

	print(cart)
	
def findCart(x1,y1,x2,y2):

	cart = math.sqrt((x2-x1)**2 + (y2-y1)**2)

	return(cart)
	
def distance (x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1 
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	print(result)

#python methods can return multiple values (tuple)
def getInput():
	x1 = int(input("Enter a value for x1: "))
	y1 = int(input("Enter a value for y1: "))
	x2 = int(input("Enter a vlaue for x2: "))
	y2 = int(input("Enter a value for y2: "))
	return x1, y1, x2, y2
	
def main():
#	solveCart()
	x1 = int(input("Enter a value for x1: "))
	y1 = int(input("Enter a value for y1: "))
	x2 = int(input("Enter a vlaue for x2: "))
	y2 = int(input("Enter a value for y2: "))
	
	print(findCart(x1,y1,x2,y2))
	
if __name__ == "__main__":
		main()    
