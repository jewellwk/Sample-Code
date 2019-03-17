class Stack:
	"""The Stack class creates an instance of a stack."""
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		self.items.pop()
		
	def size(self):
		return len(self.items)
		
	def peek(self):
		return self.items[len(self.items)-1]
		
	def getStack(self):
		for items in reversed(self.items):
			print(items)
			
def palinWord ():
	"""The palinWord method accepts a word as user input, adds each letter as an element within a Stack, and then uses a sequential search to determine if the word is a palindrome."""
	word = input("Please enter the word: ")
	letters = Stack()
	i = 0
	while i < len(word):
		letters.push(word[i])
		i += 1
	i = 0
	while i < len(word):
		if (word[i]==letters.peek()):
			letters.pop()
			palin = "This is a palindrome."
		else:
			palin = "This isn't a palindrome."
			break
		i += 1
	return palin 
	
def main():
	print(palinWord())
if __name__ == "__main__":
		main()