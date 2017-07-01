import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum1 = 0
sum2 = 0
for i in range(len(a)):
    sum1 += a[i][i]
    sum2 += a[i][len(a[0]) - 1 - i]
print(abs(sum1 - sum2))
