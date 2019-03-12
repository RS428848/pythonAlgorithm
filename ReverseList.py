def swap():
	count = len(lista)

	if count%2==1:
		x = count-1
		for y in range(0,int(count/2-0.5)):
			lista[y],lista[x]=lista[x],lista[y]
			x=x-1
		print(lista)
	else:
		x = count-1
		for y in range(0,int(count/2)):
			lista[y],lista[x]=lista[x],lista[y]
			x=x-1
		print(lista)

def append():
	count = len(lista)
	new = []
	x = 1
	for y in range(1,count+1):
		new.append(lista[int(count-x)])
		x = x+1
	print(new)
lista = input().split(",")
append()
