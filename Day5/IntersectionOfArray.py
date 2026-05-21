""" Intersection of two array. """

arr1=[1,2,3,4,5]
arr2=[4,5,6,7,8]
intersection=[]
for i in arr1:
    for j in arr2:
        if i==j:
            intersection.append(i)
print("Intersection:", intersection)