n=int(input("Enter size: "))
print("Enter list elemnet: ")
arr=[]
for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    print(arr[i])