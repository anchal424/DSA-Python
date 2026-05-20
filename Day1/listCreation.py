""" Creation of list
ls=[]
print(type(ls))

ls=list()

ls=[1,2,3,4,56,77,88]
print(type(ls))

 How to traverse a list
arr = [11,22,33,44,55,66,77,88]
print(arr)

for i in range(len(arr)):
    print(arr[i], end = " ")

print()

for x in arr:
    print(x,end=" ")

 Accessing arry in the list
arr=[11,22,33,44,55,66,77,88,99]
print(arr[3])

ans= 44"""


#-- 
arr=[11,22,33,44,55,66,77,88]
print(arr[1:5])
print(arr[5:6])
print(arr[:6])
print(arr[4:])
print(arr[:])
print(arr[::1])
print(arr[::2])
print(arr[::3]) 
print(arr[::-1])
print(arr[::-2])

