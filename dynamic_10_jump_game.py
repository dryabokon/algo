import numpy
# ----------------------------------------------------------------------------------------------------------------------
# leetcode.com/problems/jump-game/
def jump_game(A):

    if len(A)==1 and A[0]==0:
        return True

    D = numpy.full(len(A),False)
    D[0]=1

    for i in range(0,len(A)):
        if D[i]>0:
            for step in range(0,A[i]+1):
                if i+step<len(A):
                    D[i+step]=1

    return D[-1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [25000,1,1,0,0]

    res = jump_game(A)
    print(res)