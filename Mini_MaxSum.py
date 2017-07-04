# Solution to Hackerrank algorithm problem
# find the minimum and maximum sum possible from a list using len(list) - 1 numbers



arr = list(map(int, input().strip().split(' ')))
result_list = []
for i in range(len(arr)):
    sumArr = sum(arr) - arr[i]
    result_list.append(sumArr)

print(min(result_list),max(result_list))
