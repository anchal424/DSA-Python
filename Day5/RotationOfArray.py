""" Rotation Of an Array. """

arr=[1,2,3,4,5]
k=2
for i in range(k):
    temp=arr[-1]
    for j in range(len(arr)-1,-1,-1):
        arr[j]=arr[j-1]
    arr[0]=temp
print(arr)