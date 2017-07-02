def listSum(numList):
    sum = 0
    for i in numList:
        sum += i
    return sum
print (listSum([1,2,3,4,]))


# listSum using recursion
def listSumRecursion(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSumRecursion(numList[1:])

print(listSumRecursion([3,4,5,6,7,7,8]))

