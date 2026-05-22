"""
Problem Statement:

Raj wants to know the maximum marks scored by him in each semester.
The mark should be between 0 to 100, if it goes beyond the range display
“You have entered invalid mark.”

Sample Input 1:
Enter no of semester:
3
Enter no of subjects in 1 semester:
3
Enter no of subjects in 2 semester:
4
Enter no of subjects in 3 semester:
2
Marks obtained in semester 1:
50
60
70
Marks obtained in semester 2:
90
98
76
67
Marks obtained in semester 3:
89
76
Sample Output 1:
Maximum mark in 1 semester:70
Maximum mark in 2 semester:98
Maximum mark in 3 semester:89
"""



sem = int(input("Enter no of semester: "))

sub = []

for i in range(sem):
    n = int(input(f"Enter no of subjects in {i+1} semester: "))
    sub.append(n)

max_marks = []

for i in range(sem):
    maxi = 0
    print(f"Marks obtained in semester {i+1}: ")

    for j in range(sub[i]):
        mark = int(input())

        if mark < 0 or mark > 100:
            print("You have entered invalid marks. ")
            exit()

        if mark > maxi:
            maxi = mark

    max_marks.append(maxi)

for i in range(sem):

    print(f"Maximum mark in {i+1} semester:{max_marks[i]}")       
            
                