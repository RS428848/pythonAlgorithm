number = [9,4,6,3,7]

count = len(number)
new = [3]
x = 0
y = 0
for a in range(1,int(count+1)):
	
	for b in range(1,(int(many+1))):
		if number[x] < new[y]:
			new.insert(y,number[x])
			break
		else:
			new.append(number[x])
			y = y + 1
	x = x+1

print(new)