# num = 45
# sum_digits = (num // 10) + (num % 10)
# print("sum of two digits:", sum_digits)


#-- num // 10 = 4 (45 // 10)
#-- num % 10 = 5  (45 % 10)
#-- 4+5 = 9


no = int(input("Enter a number: "))
n1 = no % 10
n2 = no // 10
res = n1 + n2
print(res)