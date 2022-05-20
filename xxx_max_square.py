# https://leetcode.com/problems/maximal-square/
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# ----------------------------------------------------------------------------------------------------------------------
import numpy


def max_square(A,top=None,left=None,bottom=None,right=None):

    def is_valid(A,top,left,bottom,right):
        if top<0 or top>=A.shape[0]: return False
        if left<0 or left >= A.shape[1]: return False
        if bottom<=0 or bottom>A.shape[0]: return False
        if right<=0 or right>A.shape[1]: return False
        if (bottom-top)!=(right-left): return False
        return True

    def is_solid(A,top,left,bottom,right):
        S = A[top:bottom, left:right]
        res = numpy.min(S)==1
        return res

    def get_square(top,left,bottom,right):
        return (bottom-top)*(right-left)

    A = numpy.array(A,dtype=numpy.int32)

    if top is None:
        res = 0
        for top in range(len(A)):
            bottom = top + 1
            for left in range(len(A[0])):
                right = left + 1
                res = max(res,max_square(A,top,left,bottom,right))

    else:
        if not is_valid(A, top, left, bottom, right):return 0
        if not is_solid(A, top, left, bottom, right):return 0
        res = get_square(top, left, bottom, right)
        res = max(res,max_square(A,top-1,left-1,bottom,right))
        res = max(res,max_square(A,top-1,left,bottom,right+1))
        res = max(res,max_square(A,top, left-1, bottom+1, right))
        res = max(res,max_square(A,top, left, bottom+1, right+1))

    return res
# ----------------------------------------------------------------------------------------------------------------------
def max_square2(A):
    R, C, res = len(A), len(A[0]), 0
    for r in (range(R - 1, -1, -1)):
        for c in range(C - 1, -1, -1):
            A[r][c] = int(A[r][c])
            if r == R - 1 or c == C - 1:
                res = max(res, (A[r][c]))
            else:
                if A[r][c] == 1:
                    A[r][c] = 1 + min((A[r + 1][c]), (A[r][c + 1]), (A[r + 1][c + 1]))

                res = max(res, (A[r][c]))

    print(numpy.array(A))
    return res * res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    #A = [["0","1"],["1","0"]]

    res = max_square2(A)
    print(res)