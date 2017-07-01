myList = [1,2,3,4]# make a list
A = [myList]*3 # multiply list by 3
print(A)
myList[2]=45 # Assign element to list at position 2
print(A)
B = myList[1:3] # list slicing
print(B)
print(len(myList)) # print list length
print(len(B))
