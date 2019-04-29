import numpy
# ----------------------------------------------------------------------------------------------------------------------
# leetcode.com/problems/maximum-subarray/
def maximum_subarray(A):

    res = A[0]
    candidate = A[0]

    for i in range(1, len(A)):
        # try to contunue seria
        if candidate + A[i]>candidate:
            candidate+= A[i]
        else:
        # start new seria
            candidate = A[i]

        res = max(res, candidate)

    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('4545656756')
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    A=numpy.array(A,dtype=numpy.int)

    print(A)
    res = maximum_subarray(A)
    print(res)