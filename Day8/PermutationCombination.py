# Permutation combination problem

from itertools import permutations

def generate_permutations(num1,num2):
    number_str=str(num1)
    perm=permutations(number_str)
    perm_list=["".join(p) for p in perm]
    return [int(x) for x in perm_list if int(x) > num2]