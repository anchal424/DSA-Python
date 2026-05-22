import re
str=input("Enter a string:")
m=re.fullmatch(str,"abx@xyz_pqr*")
if m!=None:
    print("yes match found")
else:
    print("no match found")