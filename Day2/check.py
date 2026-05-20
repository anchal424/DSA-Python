"""
Question:
Accept mobile number check that number is 10 digit and digit only. 
Check number is valid in india or not. (6, 7, 8, 9)
"""

number = input("Enter your mobile number: ")
if len(number) == 10 and number.isdigit():

    if number[0] in ['6', '7', '8', '9']:
        print("Valid Indian mobile number: ")
    else:
        print("Invalid number please contact Mukesh Ambani!! ")
else:
    print("Number should contain exact 10 digits!! ")

    

