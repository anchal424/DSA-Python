# Ascending Order Merge Sort

class MergeSort:
    def merge_sort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            arr1=arr[:mid]
            arr2=arr[mid:]
            self.merge_sort(arr1)
            self.merge_sort(arr2)

            i=0
            j=0
            k=0
            while i<len(arr1) and j<len(arr2):
                if arr1[i]<arr2[j]:
                    arr[k]=arr1[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=arr2[j]
                    j+=1
                    k+=1

            while i<len(arr1):
                arr[k]=arr1[i]
                i+=1
                k+=1

            while j<len(arr2):
                arr[k]=arr2[j]
                j+=1
                k+=1

if __name__ == '__main__':
    arr=[1,7,12,3,6,2,9]
    obj=MergeSort()
    obj.merge_sort(arr)
    print(arr)