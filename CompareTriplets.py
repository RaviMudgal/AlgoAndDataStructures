import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A = B = 0
    for i in range(3):
        if a[i] > b[i]:
            A += 1
        elif a[i] < b[i]:
            B += 1
    print (str(A) + ' ' + str(B))

a0, a1, a2 = input().strip().split(' ')
a = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
#print (" ".join(map(str, result)))
