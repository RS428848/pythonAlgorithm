"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""
def rotate(list,rot):
    length = len(list)
    newList = []
    for place in range(0,length):
        newList.append(list[(place+rot+1)%length])
    print(newList)

list = [1,2,3,4,5,6,7]
rot = 3
rotate(list,rot)