import numpy
# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/minimum-path-sum/
def min_sum(A):

    A = numpy.array(A)
    R = A.shape[0]
    C = A.shape[1]

    D = numpy.zeros((R,C),dtype=numpy.int)
    D[0,0] = A[0][0]

    c=0
    for r in range(1, R): D[r, c] = D[r-1,c  ]+A[r,c]
    r=0
    for c in range(1, C): D[r, c] = D[r  ,c-1]+A[r, c]

    for r in range (1,R):
        for c in range(1, C):
            D[r,c]=A[r,c]+min(D[r-1,c],D[r,c-1])

    return D[-1,-1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [[1,3,1],[1,5,1],[4,2,1]]
    res = min_sum(A)
    print(res)