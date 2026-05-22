"""
Question: 

Capgemini in its online written test has a coding question, 
wherein the students are given a string with multiple characters that are repeated consecutively. 
You're supposed to reduce the size of this string using mathematical logic given as in the example below:
Input :
aabbbbeeeeffggg
Output:
a2b4e4f2g3

Input :
abbccccc
Output:
ab2c5
"""




Word = input("Enter String: ")
count = 1

for i in range(len(Word)):
    if i < len(Word) - 1 and Word[i] == Word[i+1]:
        count += 1
    else:
        if count == 1:
            print(Word[i], end="")
        else:
            print(Word[i] + str(count), end="")
        count = 1