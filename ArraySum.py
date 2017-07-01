import sys

def aVeryBigSum(n, ar):
    # Complete this function
    sumOfArray = sum(ar)
    return sumOfArray

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
