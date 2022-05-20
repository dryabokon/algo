# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# ----------------------------------------------------------------------------------------------------------------------
def has_dups(A):

    dct = {}
    for a in A:
        if a in dct:
            return True
        else:
            dct[a]=0
    return False
# ----------------------------------------------------------------------------------------------------------------------
def has_dups_nearby(A,k):
    dct = {}
    for i, a in enumerate(A):
        if a in dct:
            if (i - dct[a]) <= k: return True

        dct[a] = i

    return False
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [1,2,3,1]
    k = 3
    t = 0

    res = has_dups_nearby(A,k,t)
    print(res)