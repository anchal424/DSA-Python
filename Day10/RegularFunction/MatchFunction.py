""" We can use the match function to check the given pattern at begnning of target string. """

import re 
str = input("Enter any string: ")
m = re.match(str,"abc@xyz_pqr*")
if m!=None:
    print("Yes matching is available at beg")
    print('start index: ',m.start(), '. end index: ',m.end())
else:
    print("Matching is not available at beg: ")    