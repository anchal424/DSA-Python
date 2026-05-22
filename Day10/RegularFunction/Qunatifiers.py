""" We can use qunatifiers to specify the number of occurences. """

import re

x="a"
x="a+"
x="a*"
x="a?"
x="a{3}"
a="a{2,3}"

matcher=re.finditer(x,"abaababaabaaabaaaa")

for match in matcher:
    print(match.start(),'...', match.group())