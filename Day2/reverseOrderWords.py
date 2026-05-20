""" 
Program to reverse order od words.
input: Learning Python is very easy from Ashish sir
output: sir Ashish from easy very is Python Learning
"""

s = "Learning Python is very easy from Ashish sir"
words=s.split()
reverse_word = words[::-1]
result = ' '.join(reverse_word)
print(result)

