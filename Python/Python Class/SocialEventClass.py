class SocialEvent:
	"""The SocialEvent class creates an instance of an event. Each event has a a title, date, and attendees property. 
	
	Attributes:
		title: a String that represents the name of the event
		date: a String that indicates the date of the event
		attendees: an int that represents the number of attendees
	"""
	
	def __init__(self, title, date, attendees):
		"""Constructor that builds an event."""
		self.title = title
		self.date = date
		self.attendees = attendees
	
	def getTitle(self):
		"""The getTitle method returns the name of the event."""
		return self.title
		
	def getDate(self):
		"""The getDate method returns the date of the event."""
		return self.date
		
	def getAttendees(self):
		"""The getAttendees method returns the number of attendees for that event."""
		return self.attendees
	
	def setTitle(self, title):
		"""The setTitle method overrides the original title and is set by the user through the parameter 'title'."""
		self.title = title
		
	def setDate(self,date):
		"""The setDate method overrides the original date and is set by the user through the parameter 'date'."""
		self.date = date
		
	def setAttendees(self, attendees):
		"""The setAttendees method overrides the original value of attendees and is then set by the user through the parameter 'attendees'."""
		self.attendees = attendees
		
	def __str__(self):
		"""Displays the event as a String including all of its attributes."""
		return "\nEvent: " +self.title +" Date: " +self.date + " Attendees: " + str(self.attendees)

from operator import attrgetter #import that sorts a list of objects based on the object's attributes
def makeEvents():
	"""The makeEvents method prompts the user for necessary input until 5 SocialEvent objects are created. A list is then returned containing the objects."""
	events = list()
	i = 0
	while i < 5:
		name = input("Enter the name of the event: ")
		date = input("Enter the date of the event: ")
		numppl = input("How many people will be attending: ")
		numatd = int(numppl) #explicitly typecasts the attendees field to an int
		event = SocialEvent(name,date,numatd)
		events.append(event) #adds each object to the list
		i+=1
	return sorted(events, key=attrgetter('attendees')) #sorts the list of objects based on the attendees property

	
def main () :
	yourEvents = makeEvents() #invokes the makeEvents method and initializes a list called 'yourEvents'
	
	for i in yourEvents: #loop that iterates through the 'yourEvents' list and prints each object
		print(i)

if __name__== "__main__":
	main()