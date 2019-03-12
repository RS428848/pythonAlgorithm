class Person(object):
	def __init__(self,firstname,lastname,age):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
	def setAge(self):
		newAge = int(input("Enter a positive integer: "))
		self.age = newAge
	def setAgeTwo(self,newAge):
		self.age = newAge
	def name(self):
		return(self.firstname + " "+ self.lastname)
	def getFirstName(self):
		return(self.firstname)
	def getLastName(self):
		return("your last name is:" + self.lastname)
	def getAge(self):
		return(self.age)
