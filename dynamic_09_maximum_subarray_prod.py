# https://leetcode.com/problems/maximum-product-subarray/
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# ----------------------------------------------------------------------------------------------------------------------
def maximum_subarray_prod(A):

    res = A[0]
    imax = A[0]
    imin = A[0]

    for i in range(1,len(A)):
        if A[i] < 0:
            imax, imin =imin,imax

        imax = max(A[i], imax * A[i])
        imin = min(A[i], imin * A[i])
        res = max(res, imax)



    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = [-3,-1,-1]
    res = maximum_subarray_prod(A)
    print(res)