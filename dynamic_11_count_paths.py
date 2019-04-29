import numpy
# ----------------------------------------------------------------------------------------------------------------------
# leetcode.com/problems/unique-paths/
def count_paths(R,C):

    D = numpy.zeros((R,C),dtype=numpy.int)
    D[0,:] = 1
    D[:,0] = 1
    for r in range (1,R):
        for c in range(1, C):
            D[r,c]=D[r-1,c]+D[r,c-1]

    return D[-1,-1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    res = count_paths(7,3)
    print(res)