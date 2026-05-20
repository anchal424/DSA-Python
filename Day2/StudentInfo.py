"""
Question:
Taking input from user as number of students their marks, 
percentage and then displaying it in dictionary form.
"""

rec={}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    per = float(input("Enter perc: "))
    rec[name] = per

print(rec)
for x in rec:
    print(x, "\t", rec[x])