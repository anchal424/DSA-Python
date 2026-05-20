""" Remove duplicate from unsorted Arrays:
Write a function to remove duplicates from an unsorted array. 
Input: [3,2,3,1,2,4]
output: [3,2,1,4] """\

arr = [5, 3, 9, 2, 3, 5]

newArr = []

for i in range(len(arr)):

    if arr[i] not in newArr:
        newArr.append(arr[i])

print(newArr)