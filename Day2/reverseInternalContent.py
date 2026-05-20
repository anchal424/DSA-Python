"""
Program to reverse internal content of each word.
input: Learning Python is very easy from Ashish Sir.
output: gninraeL nohtyP si yrev ysae morf hsihsA riS
"""

s = "Learning Python is very easy from ashish sir. "
word = s.split()
for i in word:
    print(i[::-1], end=" ")



s = "Learning Python is very easy from Ashish Sir"
words = s.split()

newList = []

for i in words:
    newList.append(i[::-1])
print(" ".join(newList))
