alist = [56,34,12,0,4,-2]

for a in range(1,len(alist)):
	place = 0
	for b in range(1,len(alist)):
		if alist[place]>alist[place+1]:
			alist[place],alist[place+1] = alist[place+1],alist[place]
			
		place = place + 1
	
print(alist)