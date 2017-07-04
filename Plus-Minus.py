# Solution to Hackerrank algorithm problem
# calculate percentage of positive numbers, negative numbers and zeros in a file
# sample file
# 6 (number of records in file)
# -4 -1 0 3 -4 0 (records)

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def calc(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))


(calc(arr))
