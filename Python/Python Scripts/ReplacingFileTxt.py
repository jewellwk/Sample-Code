#This program reads a file and replaces all the four character words with '****' and outputs to a text file called "Output". 
def main():
	file = input("Type file name: ")	
	filein = open(file)
	fileout= open("Output.txt",'w')
	filecontent = ""		
	for line in filein:					#reads the file per line
		checkline = line.split(' ') 	#splits each line into a list of words
		for i in checkline:				#checks each word
			if len(i) == 4:				
				ind = checkline.index(i)
				checkline.remove(i)
				checkline.insert(ind,'****')
		for i in checkline:				#converts list to String
			filecontent += i + ' '
	fileout.write(filecontent)			#outputs the String to a file
	filein.close()
	fileout.close()
	
if __name__ == "__main__":
	main()