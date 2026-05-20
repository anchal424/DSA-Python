def binary_search(n, arr, target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            flag=True
            loc=mid
            break;
        elif target<arr[mid]:
            high=mid-1
        elif target>arr[mid]:
            low=mid-1
    if flag==True:
        print("Element found at index: ", mid)
    else:
        print("Element not found.")

if __name__ == '__main__':
    n = int(input("Enter size: "))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    target=int(input("Enter no which is to re searched: "))
    binary_search(n, arr, target)