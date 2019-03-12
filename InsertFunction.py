alist = [1,3,5,7,9]

y = 2
x = 4
def insert():
	count = len(alist)-1
	z = count
	alist.append(alist[count])
	for a in range(1,count-y+1):
		alist[z] = alist[z-1]
		z = z-1
	alist[y]=x
	print(alist)

def combine():
	asplit = []
	bsplit = [x]
	csplit = []
	h = 0
	k = y
	for a in range(1,y+1):
		asplit.append(alist[h])
		h = h+1
	for c in range(1,len(alist)-y+1):
		csplit.append(alist[k])
		k = k+1
	new =asplit + bsplit + csplit
	print(new)
	
combine()