""" Find the maximum and minimum elements:
Write a function to find the maximum and minimum
elements in an array.
input:[5,3,9,2,8]
output: maximum: 9, minimum: 2 """

arr = [11,22,33,44,55,66,77,88]

max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]

    if min > arr[i]:
        min = arr[i]

print("Maximum:", max)
print("Minimum:", min)