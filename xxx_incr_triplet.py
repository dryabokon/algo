# https://leetcode.com/problems/increasing-triplet-subsequence/
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
# ----------------------------------------------------------------------------------------------------------------------
def incr_triplet_exists(A):

    def incr_pair_exists(A):
        for i1 in range(0, len(A) - 1):
            temp_A = [A[i] for i in range(i1 + 1, len(A)) if A[i] > A[i1]]
            if len(temp_A) >= 1: return True
        return False

    for i1 in range(0,len(A)-2):
        temp_A = [A[i] for i in range(i1+1,len(A)) if A[i]>A[i1]]
        if len(temp_A)<2:continue
        if incr_pair_exists(temp_A):
            return True

    return False
# ----------------------------------------------------------------------------------------------------------------------
def incr_triplet_exists2(A):

    small = smallest = float('Inf')
    for n in A:
        if   n <= smallest:smallest = n
        elif n <= small:small = n
        else:return True
    return False

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = [5,4,3,2,1]

    res = incr_triplet_exists2(A)
    print(res)
