"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""
def move_zeros(array):
    lenArray = len(array)-1
    zeroValue = []
    for value in range(lenArray):
        if array[value] == 0:
            zeroValue.append(value)
    lenZero = len(zeroValue)
    placeValue = 0
    a = 0
    while lenZero>0:
        array.append(0)
        del array[zeroValue[placeValue]-a]
        a = a+1
        lenZero = lenZero-1
        placeValue = placeValue + 1
    print(array)
array = ["false", 1, 0, 1, 2, 0, 1, 3, "a"]
move_zeros(array)