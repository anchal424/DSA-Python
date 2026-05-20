n=int(input("Enter size: "))
print("Enter list element: ")
sum=0
arr=[]
for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)
    
for i in range(len(arr)):
    sum=sum+arr[i]
    print(sum)
    