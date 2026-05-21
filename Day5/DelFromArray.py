""" Delete an element from Array. """

arr=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
loc=int(input("Enter location to delete: "))
for i in range(loc+1, len(arr)):
    arr[i-1]=arr[i]
arr.pop()
print(arr)