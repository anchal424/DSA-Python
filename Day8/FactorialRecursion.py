# Factorial using recursion

def fact(n=1):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '_main_':
    n=5
    res=fact(n)
    print(res)