from InheritancePerson import Person
class Employee(Person):
	def __init__(self,firstname,lastname,age,salary):
		Person.__init__(self,firstname,lastname,age)
		self.salary = salary
	def getSalary(self):
		return(self.salary)