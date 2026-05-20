n=int(input("Enter size: "))
print("Enter list element: ")
sum=0
even =0
odd=0
arr=[]
for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)
for i in range(len(arr)):
    if arr[i] %2==0:
        even=even+arr[i]
    else:
        odd=odd+arr[i]
print("even",even)
print("odd",odd)