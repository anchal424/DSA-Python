"""
Find sum of natural numbers using recursion.
"""

def sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
         return n + sum(n-1) 


if __name__ == '__main__':
    n=5
    res=sum(n)
    print(res)


