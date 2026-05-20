no = int(input("Enter no: "))
n1=0
n2=0
save=no
sum =0
count=0
while no>0:
    no= no//10
    count = count+1
no=save
if count%2==0:

    mid=count//2
n1 = no % 10**mid
n2 = no // 10** mid
sum=n1+n2
sq=sum*sum
if sq==no:
    print("Tech")
else:
    print("Nontech")