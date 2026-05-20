"""Functions with parameters with return"""

def add(a,b):
    res=a+b
    return res

if __name__ =='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r=add(a,b)
    print("Addition is",r)