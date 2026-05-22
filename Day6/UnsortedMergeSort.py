# Merge sort for unsorted Array

class MergeSort:
    def mergesort(self,arr1,arr2):
        arr3=[]
        i=0
        j=0
        k=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr3.append(arr1[i])
                i+=1
                k+=1
            else:
                arr3.append(arr2[j])
                j+=1
                k+=1
        while len(arr1)>i:
            arr3.append(arr1[i])
            i+=1
            k+=1

        while len(arr2)>j:
            arr3.append(arr2[j])
            j+=1
            k+=1
        return arr3

if __name__ == '__main__':
    obj=MergeSort()
    arr1=[1,3,5,6,7,9]
    arr2=[2,4,8]
    ans=obj.mergesort(arr1,arr2)
    print(ans)