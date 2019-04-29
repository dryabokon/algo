import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
# ----------------------------------------------------------------------------------------------------------------------
def find_pythagorian_triplet(A):

    AA = numpy.array([a*a for a in A])
    idx = numpy.argsort(-AA)
    AA = AA[idx]
    for i in range(0,A.shape[0]-2):
        left = i+1
        right = A.shape[0]-1
        while left<right:
            S = AA[left] + AA[right]
            if S==AA[i]:
                print(A[idx[left]],A[idx[right]],A[idx[i]])
                right -= 1
                left+=1
            elif S<AA[i]:
                right-=1
            else:
                left+=1

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = numpy.array(list('34571235686784575675'),dtype=numpy.int)

    res = find_pythagorian_triplet(A)
    print(res)
