num = int(input("Enter a number: "))
num1 = num % 10
num = num // 10
num2 = num % 10
num = num // 10
num3 = num % 10
res = num1 + num2 + num3
print(res)