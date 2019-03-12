from InheritanceEmployee import Employee
class Intern(Employee):
	def __init__(self,firstname,lastname,age,salary,college):
		Employee.__init__(self,firstname,lastname,age,salary)
		self.college = college
	def getCollege(self):
		return(self.college)