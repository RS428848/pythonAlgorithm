#Find the index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array.
#Returns index of 0 to be replaced with 1 to get longest continuous sequence of 1s. If there is no 0 in array, then it returns -1.
    #e.g.
    #let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    #If we replace 0 at index 3 with 1, we get the longest continuous
    #sequence of 1s in the array.
    #So the function return => 3
def f(array):
    zeroIndex = []
    countOne =[]
    mergeCounter = []
    answer = 0
    for index in range (0,len(array)-1):
        if array[index] == "0":
            zeroIndex.append(index)
    if len(zeroIndex) == 0:
        print(-1)
        return
    elif len(zeroIndex)==1:
        print(zeroIndex[0])
        return
    else:
        countOne.append(zeroIndex[0])
        for a in range(1,len(zeroIndex)):
            countOne.append(zeroIndex[a]-zeroIndex[a-1]-1)
        countOne.append(len(array)-zeroIndex[-1]-1)
    for zero in range(0,len(zeroIndex)):
        mergeCounter.append(countOne[zero]+countOne[zero+1]+1)
    for c in range(0,len(mergeCounter)-1):
        if mergeCounter[c+1]>mergeCounter[c]:
            answer = zeroIndex[c+1]
        elif mergeCounter[c+1] == mergeCounter[c]:
            answer= zeroIndex[c+1]
            answer = zeroIndex[c]
    print(answer)
array_string = input("Enter a list by typing the elements with spaces: ")
array = array_string.split()
f(array)
