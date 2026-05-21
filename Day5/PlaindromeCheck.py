"""plaindrome string checking"""

s="A man, a plan, a canal: Panama"
str=""
for x in s:
    if x.isalpha():
        str+=x.upper()
if str==str[::-1]:
    print("valid Palindrome")
else:
    print("Not a palindrome")