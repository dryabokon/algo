# ----------------------------------------------------------------------------------------------------------------------
def get_min_health(A):
    import numpy
    R, C = len(A), len(A[0])

    H_crd = numpy.full((R+1,C+1),numpy.inf)
    H_crd[R - 1][C], H_crd[R][C - 1] = 1, 1
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            H_crd[r][c] = max(min(H_crd[r + 1][c], H_crd[r][c + 1]) - A[r][c], 1)

    print(numpy.array(A))
    print()
    print(H_crd)

    return int(H_crd[0][0])
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    #A  = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
    #A = [[0, 0, 0], [1, 1, -1]]

    res = get_min_health(A)
    print(res)