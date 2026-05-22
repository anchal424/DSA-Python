import re
number = input("Enter mobile number: ")
match = re.fullmatch("[6-9]\\d{9}",number)
if match != None:
    print(number, "is valid mobile number")
else:
    print(number, "is not valid mobile number")    