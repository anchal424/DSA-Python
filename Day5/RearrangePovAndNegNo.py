""" Rerrange positive and negetive numbers in an array. """


arr=[-1,2,-3,4,5,-6]
arr2=[]
arr3=[]
answer=[]
for i in range(len(arr)):
    if arr[i]>0:
        arr2.append(arr[i])
    else:
        arr3.append(arr[i])
print(arr2, arr3)

for i in range(len(arr2)):
    answer.append(arr2[i])
    answer.append(arr3[i])
print(answer)