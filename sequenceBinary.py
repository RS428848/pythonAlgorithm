
#Find the index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array.
#Returns index of 0 to be replaced with 1 to get longest continuous sequence of 1s. If there is no 0 in array, then it returns -1.
    #e.g.
    #let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    #If we replace 0 at index 3 with 1, we get the longest continuous
    #sequence of 1s in the array.
    #So the function return => 3

array = [1,1,1,0,1,1,1,1,1,0,1,1]
orgArray = [1,1,1,0,1,1,1,1,1,0,1,1]
count = 0
zeroIndex = []
for a in range(0,len(array)):
    if array[a] == 0:
        zeroIndex.append(a)
        
lengthZero = len(zeroIndex)-1
totalCount = {}
finalAnswer = []
while lengthZero >= 0:        
    array.insert(zeroIndex[lengthZero],1)
    del array[zeroIndex[lengthZero]+1]

    actualCount = count
    for b in range(0,len(array)):
        if array[b] == 1:
            count += 1
            if count>actualCount:
                    actualCount = count
            else:
                actualCount = actualCount
        else:
            count = 0
    totalCount[actualCount] = zeroIndex[lengthZero]
    finalAnswer.append(actualCount)
    array = orgArray
    count = 0
    lengthZero -= 1
    
finalAnswer.sort()
finalAnswer.reverse()

print (totalCount.get(finalAnswer[0]))




