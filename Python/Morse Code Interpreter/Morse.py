def stringtoMorsecode(n):
	result = ""
	normalAlpabet = list("abcdefghijklmnopqrstuvxyz")
	morseAlphabet = ['.-','-...','-.-','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----']
	for i in range(0, len(n)):
		for j in range(0, len(normalAlpabet)):
			if(n[i] == normalAlpabet[j]):
				result += morseAlphabet[j]
				
		result += ' '
		if(n[i] == ' '):
			result += '\\ '
	return result
	
def main():
	
	print(stringtoMorsecode("i love you"))
	
if __name__ == "__main__":
	main()