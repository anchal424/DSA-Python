num = int(input("Enter a number: "))
rev = 0
save = num
while num>0:
    rem = num % 10
    rev = rev*10+rem
    num = num // 10

if rev == save:
    print("Number is palindrome: ")
else:
    print("number is not palindrome")
    