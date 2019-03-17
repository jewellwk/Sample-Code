"""The read_nums method attempts to open a file called numbers.txt. If the file is in read mode then it reads each value in the file line by line and writes each value to a new file called output_average.txt. Also, as each value is written into output_average.txt, it is typecasted to an integer and stored into a list called list_ints. Lastly, the method calulates the average of the values, writes them to output_average.txt, and closes both files"""
def read_nums():
	try:
		numbers = open("numbers.txt", "r") #file with data
		average = open("output_average.txt", "w+") #new file
		ten_ints = []
		if numbers.mode == 'r': #checks mode of the numbers.txt file
			num = numbers.readlines()
			list_ints = []
			i = 0 #acts as the index
			#write each value to the file and appends the value as an int to the list called list_ints
			for x in num:
				average.write('\nNumber: {value}'.format(value = num[i].strip("\n")) )
				list_ints.append(int(num[i].strip("\n")))
				i+=1
		#writes the average of the values to the output_average.txt file
		average.write("\nThe average of these numbers is = {nums_average}".format(nums_average = (sum(list_ints)/len(list_ints))))
		#closes each file
		average.close()
		numbers.close()
	except IOError:
		print("An error occurred trying to read the numbers.txt file.")
		
	except ValueError:
		print("Non-numeric data found in the file.")
		
	except:
		print("An error occurred. ")
	
def main():
	read_nums()
	
if __name__ == "__main__":
	main()