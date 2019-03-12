'''
Robert Song
atesting.py
10/26/18
The program helps the user compute the distance between two gemetric points
'''
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)
x1 = float(input("Enter a number to be your first x point: "))
y1 = float(input("Enter a number to be your first y point: "))
x2 = float(input("Enter a number to be your second x point: "))
y2 = float(input("Enter a number to be your second y point: "))

print("The distance between the two geometric point is: ",distance(x1,x2,y1,y2))
