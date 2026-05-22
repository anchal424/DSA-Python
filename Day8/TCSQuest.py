"""
Compute the nearest largest number by interchanging its digits updated.
Given 2 numbers a and b find the smallest number greater than b by interchanging the 
digits of a and if not possible print -1.
Input Format: 2 numbers a and b, seperated by space.
Output Format: A single number greater than b. If not possible, print -1.
Constraints: 1 <= a, b <= 1000000

Example 1:
Input: 459 500
Output: 549

Example 2:
Input: 645757 457765
Output: 465577

Explaination: 
Input: a = 459
       b = 500
permutation of 459
valid number greater than 500
smallest valid number.       
"""



def find_permutation(digits, path, used, perm):
    if len(path) == len(digits):
        num = int(path)
        perm.append(num)
        return

    for i in range(len(digits)):
        if used[i] == False:
            used [i] = True
            find_permutation(digits, path + digits[i], used, perm)
            used[i] = False

def smallest_greater(a, b):
    digits = list(str(a))
    used = [False] * len(digits)
    perm = []

    find_permutation(digits, "", used, perm)

    ans = []

    for num in perm:
        if num > b:
            ans.append(num)

    if len(ans) == 0:
        print(-1)
    else:
        print(min(ans))


if __name__ == '__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    smallest_greater(a, b)



