"""
WAP to remove duplicate characters from the given input string
input: ABCDABBCDCCDEEEF
output: ABCDEF
"""

s = "ABCDABBCDCCDEEEF"
newString = ""

for i in s:
    if i not in newString:
        newString = newString + i

print(newString)