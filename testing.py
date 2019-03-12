array = [1,1,1,0,1,1,1,1,1,0,1,1]
count = 0
zeroIndex = []
for a in range(0,len(array)):
    if array[a] == 0:
        zeroIndex.append(a)
