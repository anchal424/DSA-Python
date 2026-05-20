
"""Functions with parameters with return multiple values"""

def add(a,b):
    res=a+b
    res2=a-b
    res3=a*b
    return res,res2,res3

if __name__ =='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r,r2,r3=add(a,b)
    print("Addition is",r)
    print("subtraction is",r2)
    print("Multiplication  is",r3)