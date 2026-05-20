#-- WAP to accept cost price from user and ask whether the user is a student or not. 
#-- If the user is student and cost price is greater than 500, give discount of 10% else discount will be 5%.
#-- If user is not student and cost price is greater than 500 then give discount of 8% else discount will be 2%.


cp = int(input("Enter cost price: "))
st = input("Are you student? (yes/no): ")

if st == "yes":
    if cp>500:
        discount = cp * 0.10
    else:
        discount = cp * 0.5
else:
    if cp>500:
        discount = cp * 0.8
    else:
        discount = cp * 0.2

FinalDiscount = cp - discount
print("Discount: ", FinalDiscount)


 
