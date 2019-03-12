from InheritancePerson import Person
from InheritanceEmployee import Employee
from InheritanceIntern import Intern
x = Person("Robert","Song",14)
y = Employee("Yukuan","Smith",50,100000)
z = Intern("Bob","Brown",22,50000,"University of Maryland")
print(x.name())
print(y.name())
print(y.getSalary())
print(z.name())
print(z.getSalary())
print(z.getCollege())

