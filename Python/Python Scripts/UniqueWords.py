#This program prompts the user to enter a sequence of words and then displays a list of the unique words (words that are not repeated).
words = input("Enter the words you would like: ")
checkWords = words.split(" ")
uniqueWords = list()
i = 0
while i < len(checkWords):
	count = checkWords.count(checkWords[i])
	if count == 1:
			uniqueWords.append(checkWords[i])
	i = i + 1 
print(uniqueWords)

	