import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def next_permutation(A):

    L = len(A)
    i=L-2
    success = False
    while success == False:

        # find decreasing element
        while (i>=0) and (A[i]>A[i+1]):i-=1
        if i>=0:
            #find elements in right > A[i]
            j=L-1
            while (j>i) and (A[i]>=A[j]):
                j-=1
            if j>i:
                A[i],A[j] = A[j],A[i]
                temp = A[i + 1:]
                temp.sort()
                A[i+1:]=temp
                success= True
            else:
                success = False
                i-=1
        else:
            A.sort()
            success = True

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = numpy.array(list('1'),dtype=numpy.int)
    #A = [2, 2, 7, 5, 4, 3, 2, 2, 1]
    print(A)
    next_permutation(A)
    print(A)
