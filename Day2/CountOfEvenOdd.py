n=int(input("Enter size: "))
print("Enter list element: ")
sum=0
even =0
odd=0
o1=0
e1=0
arr=[]
for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)
for i in range(len(arr)):
    if arr[i] %2==0:
        even=even+arr[i]
        el=e1+1
    else:
        odd=odd+arr[i]
        o1=o1+1

print("even",even)
print("odd",odd)
print(e1)
print(o1)