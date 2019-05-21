
"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""
def SummaryRanges(array):
    length = len(array)-1
    rangeList =[]
    count = 0
    b = array[0]
    for x in range(0,length):
        if array[x]+1==array[x+1]:
            b = b + 1
            count =count + 1
        else:
            a = b-count
            rangeList.append([a,b])
            b = array[x+1]
            count = 0
    if array[-1] != array[-2]:
        rangeList.append([array[-1],array[-1]])
    print(rangeList)

array = [0,1,2,4,5,7]
SummaryRanges(array)


