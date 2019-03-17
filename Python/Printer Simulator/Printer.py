"""This is a printer simulation program that accepts a file as the parameters for a printing lab."""
import random #imports random object generator

"""Method that allows the user to enter the name of a file, reads the file, copies each value into a list, and returns the list."""
def inandoutfile():
	data = list ()
	fin = None
	try:
		file = input("Type file name: ") #user inputs file's name
		fin = open(file)
		for line in fin: #iterates through the file line by line
			s_line = line.strip() #strips extra spaces from each line
			data.append(s_line) #adds each line's value to a list
		return data 
	except IOError as e: #exception for if the file is not found
		print(e)
		quit()
	finally:
		if fin is not None:
			fin.close() #closes the orginal file if one was opened
			
info = inandoutfile() #initializes the list from the input file to a variable
i = 0
while True and i < len(info): #loop that checks each value in the list to confirm it is an integer
	try:		
		n = int(info[i])
		i += 1
	except ValueError:
		print("One of your values aren't integers, a value is missing, or there is an empty line! Please fix your file ...")
		quit()
#series of if statements that ensures each value meets certain conditions
if (int(info[0]) > 36000 or int(info[0]) < 3600):
	print("The duration of the simulation must be between 3600-36000. Please fix the first value. Exiting")
	quit()
if (int(info[1]) > 100 or int(info[1]) < 1):
	print("The number of simulation must be whole numbers between 1 and 100. Please adjust the second value. Exiting.")
	quit()
if (int(info[2]) > 100 or int(info[1]) < 1):
	print("The minimum task size must be between 1 and 100. Please adjust the third value. Exiting.")
	quit()
if (int(info[3]) > 100 or int(info[1]) < 1):
	print("The maximum task size must be between 1 and 100. Please adjust the fourth value. Exiting.")	
	quit()
if(int(info[4]) > 2 or int(info[4]) < 1):
	print("The number of printers must be 1 or 2. Please adjust the fifth value. Exiting.")
	quit()
if (int(info[5]) > 50 or int(info[5]) < 1):
	print("The number pf pages per minute must be between 1 and 50.")
	quit()
	
"""The Queque class generates a Queque object to be used to store tasks"""
class Queue:
	def __init__(self):
		self.items = []
		
	def is_Empty(self):
		return self.items == []
		
	def enqueue(self,item):
		self.items.insert(0,item)
	
	def dequeue(self):
		return self.items.pop()
		
	def size(self):
		return len(self.items)
		
	def getItems(self):
		for i in reversed(self.items):
			print(i)
"""The Printer class generates Printer objects that are used in the simulation."""
class Printer:
	def __init__(self,ppm):
		self.page_rate = ppm
		self.current_task = None
		self.time_remaining = 0
		
	def ppm(self): #added ppm method that returns the page per minute rate of the Printer object
		return self.page_rate
	
	def tick(self):
		if self.current_task != None:
			self.time_remaining -= 1
			if self.time_remaining <= 0:
				self.current_task = None
	def busy(self):
		if self.current_task != None:
			return True
		else:
			return False
			
	def start_next(self, new_task):
		self.current_task = new_task
		self.time_remaining = new_task.getPages()*60/self.page_rate
"""The Task class generates tasks based on the time and user input from the file dictating the range for the minimum and maximum task size."""		
class Task:
	def __init__(self,time):	
		self.timestamp = time	
		self.pages = random.randrange(int(info[2]),int(info[3])+1)
		
	def getStamp(self):
		return self.timestamp
		
	def getPages(self):
		return self.pages
		
	def waitTime(self,current_time):
		return current_time-self.timestamp

fout= open("sim_out.txt",'a') #creates and then opens a new text file called "sim_out" and adds to the file.

"""The newPrintTask method randomly and continuousyly generates new tasks."""
def newPrintTask():
	num = random.randrange(1,181)
	if num == 180:
		return True
	else:
		return False
"""The simulation method functions as if it were the printing lab."""		
def simulation(numSec, pagesPerMin):
	labprinter = Printer(pagesPerMin) #initializes first Printer
	printQue = Queue() #normal Queque that holds printing tasks
	idleQ = Queue() #idle Queque that holds tasks if there are two printers and both are busy
	waitingtimes = [] #list that stores wait times
	if (int(info[4]) == 2): #checks to see if there is more than one printer
		if (int(info[6]) < 50 and int(info[6]) > 1):
			labprinter2 = Printer(int(info[6]))  #if more than one printer is necessary then the second printer is initialized.
		else:
			print("Invalid input for the page per minute for the second Printer. Please input a value between 1 and 50. Exiting")
			quit()
		for currentSecond in range(numSec): #loop that runs the simulation
				if newPrintTask():
					task = Task(currentSecond)
					printQue.enqueue(task)
					#if both printers are not busy then the printer with the higher ppm receives the task. The default printer is the first printer if the ppms are the same
				if (not labprinter.busy()) and (not labprinter2.busy()) and (not printQue.is_Empty()):
					if int(labprinter.ppm()) >= int(labprinter2.ppm()):
						if (not idleQ.is_Empty()):
							nexttask = idleQ.dequeue()
						else:
							nexttask = printQue.dequeue()
						waitingtimes.append(nexttask.waitTime(currentSecond))
						labprinter.start_next(nexttask)
				#if the first Printer is busy and the second Printer is not then the task is sent to the second Printer 
				elif (labprinter.busy()) and not labprinter2.busy() and (not printQue.is_Empty()):
					if (not idleQ.is_Empty()):
						nexttask = idleQ.dequeue()
					else:
						nexttask = printQue.dequeue()
					waitingtimes.append(nexttask.waitTime(currentSecond))
					labprinter2.start_next(nexttask)
				#if the second Printer is busy and the first Printer is not then the task is sent to the first Printer
				elif (not labprinter.busy()) and labprinter2.busy() and (not printQue.is_Empty()):
					if (not idleQ.is_Empty()):
						nexttask = idleQ.dequeue()
					else:
						nexttask = printQue.dequeue()
					waitingtimes.append(nexttask.waitTime(currentSecond))
					labprinter.start_next(nexttask)
				#if both Printers are busy then the task is sent to the idle Queue
				elif (labprinter.busy()) and labprinter2.busy() and (not printQue.is_Empty()):
					nexttask = printQue.dequeue()
					idleQ.enqueue(nexttask)
							
				labprinter2.tick()					
				labprinter.tick()
	else:
		#default statement that runs the simulation with the first Printer only
		for currentSecond in range(numSec):
			if newPrintTask():
				task = Task(currentSecond)
				printQue.enqueue(task)

			if (not labprinter.busy()) and (not printQue.is_Empty()):
				nexttask = printQue.dequeue()
				waitingtimes.append(nexttask.waitTime(currentSecond))
				labprinter.start_next(nexttask)

			labprinter.tick()

	average_wait = sum(waitingtimes)/ len(waitingtimes)
	fout.write("Average wait: %6.2f secs %3d tasks remaining."
	%(average_wait, printQue.size()))
	fout.write("\n")
	#returns the average wait to be used in calculation in the overall average wait
	return average_wait

"""The main method acts as a driver for the simulation."""
def main():	
	total = 0
	#runs the simulation a quantity of times based on data from the original input file					
	for i in range(int(info[1])):
		total += simulation(int(info[0]),int(info[5]))
	#calculates and writes the overall wait to the created file
	fout.write("Overall average wait time: %6.2f secs"
			%(total/int(info[1])))
	#closes the file
	fout.close()
	
if __name__ == "__main__":
	main()
					
		
		