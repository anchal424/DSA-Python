"""
arr=[11,22,33]
print(arr)
for i in range(len(arr)):
    print(arr[i])
"""

arr=[[1,2,3],22,[4,5]]
print(arr)
for i in range(len(arr)):
    print(arr[i])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
        print()