#method that stores each character from a String into a dictionary based on the count of that character
def storeChars (abc): 
	chars = dict ()
	i = 0
	while i < len(abc):
		letter = abc [i]
		chars[letter] = abc.count(letter)
		i = i + 1
	return chars
#method that compares the characters	
def checkChars (a,b,c):
	i = 0 
	while i < len(b):
		if a.get(c[i], 0) >= b.get(c[i],0):
			check = True
		else:
			check = False
			break
		i = i + 1
	if (check):
		print(True, "- You have enough characters.")
	else:
		print(False, "- You do not have enough characters.")
#creates two dictionaries and then uses the original String to determine if the necessary characters are present		
def main():
	mag = input ("Insert the text of the magazine: ")
	a = storeChars(mag)
	ran = input("Enter the desired ransom note: ")
	b = storeChars(ran)
	checkChars(a,b, ran)
	
if __name__ == "__main__":
	main()