file = open("testfile.txt", "r") 
lines = file.readlines()
for line in lines:
	words = line.split(" ")
	for a in words:
		if a == "ello":
			print("I found it!")
		else:
			print("I did not")
file.close() 