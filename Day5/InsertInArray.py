""" Insert an element in Array. """

arr=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
key=int(input("Enter element to insert: "))
loc=int(input("Enter location to insert: "))
arr.append(0)
for i in range(len(arr)-2 ,loc+1):
    arr[i]=arr[i+1]
arr[loc]=key
print(arr)