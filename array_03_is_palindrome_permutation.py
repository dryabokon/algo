# Given a string, write a function to check if it is a permutation of a palindrome.
# Input: Tact Coa
# Output: True (permutations: "taco cat'; "atc o eta·; etc.)
# ----------------------------------------------------------------------------------------------------------------------
import collections
# ----------------------------------------------------------------------------------------------------------------------
def is_palindrome_permutation(A):

    dct = collections.Counter(A.lower())
    cnt = 0
    res = True
    for key,val in dct.items():
        if key==' ':continue
        if val%2==1:
            if cnt>0:
                res = False
                break
            else:
                cnt = 1

    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = 'Tact Coarr'

    res = is_palindrome_permutation(A)
    print(res)