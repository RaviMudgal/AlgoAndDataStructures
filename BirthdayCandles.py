# Solution to Hackerrank algorithm problem
# Given the  for each individual candle, find and print the number of candles that can be successfully blown out.
#  Only candles with maximum height can be blown out
# input format
# The first line contains a single integer, , denoting the number of candles on the cake.
# The second line contains  space-separated integers, where each integer  describes the height of candle .
# 6
# 1 3 4 3 4 4

def birthdayCakeCandles(n, ar):
    # Complete this function
    maximum_height = max(ar)
    count = 0
    for i in ar:
        if maximum_height == i:
            count += 1
    return count


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
