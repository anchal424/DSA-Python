num = int(input("Enter a three digit number: "))
num1 = num % 10
num = num // 10
num2 = num % 10
num = num // 10
num3 = num % 10

rev = num1*100 + num2*10 + num3*1
print(rev)

# 300
#  20
#   1
# ----
# 321