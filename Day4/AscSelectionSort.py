""" Selection sort in Ascending order. """

def selectionsort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if min>arr[j]:
                min=arr[j]
                loc=j
        arr[i],arr[loc]=arr[loc],arr[i]
    
if __name__ == '__main__':
    arr=[6,23,2,4,1,8,56,3]
    selectionsort(arr)
    print(*arr)