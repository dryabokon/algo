# https://leetcode.com/problems/search-a-2d-matrix-ii
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# ----------------------------------------------------------------------------------------------------------------------
def srch(A,target):
    c = -1
    for Row in A:
        while c + len(Row) and Row[c] > target:
            c -= 1
        if Row[c] == target:
            return True
    return False
# ----------------------------------------------------------------------------------------------------------------------
def srch2(A,target):

    for V in A:
        for a in V:
            if a == target:
                return True
    return False
# ----------------------------------------------------------------------------------------------------------------------
def srch3(A,target):
    C,R = len(A[0]),len(A)
    col = C-1
    row =0
    while (col >= 0 and row <= R - 1):
        if target == A[row][col]:return True
        elif (target < A[row][col]):
            col-=1
        else:
            row+=1
    return False
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    A = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    res = srch3(A,target)
    print(res)