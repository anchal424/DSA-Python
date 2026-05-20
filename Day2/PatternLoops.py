""" nested loop 
Outer loop represents ROWS
Inner loop represents Colls 
pattern is:   j1 j2 j3 j4
           i=1 1  1  1  1
           i=2 2  2  2  2
           i=3 3  3  3  3
           i=4 4  4  4  4  """

"""
for i in range(1,5):
    for j in range(1,5):
        print(i, end = " ")
    print()   
"""

"""
1        2       3       4       
5        6       7       8       
9        10      11      12      
13       14      15      16 
"""

"""
n=1
for i in range(1,5):
    for j in range(1,5):
        print(n, end = "\t ")
        n=n+1
    print()   
"""


"""
n=65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n), end = "\t ")
        n=n+1
    print()
"""

"""
1
22
333
4444
"""

"""
for i in range(1,5):
    for j in range(1,i+1):
        print(i, end = " ")
    print()
"""

"""

****
***
**
*

"""

"""
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*", end = " ")
    print()
"""


"""
****
 ***
  **
   *
"""

sp=0
for i in range(4,0,-1):
    for x in range(sp):
        print(" ",end="")
    for j in range(1,i+1):
        print("*", end = "")
    print()
    sp=sp+1
