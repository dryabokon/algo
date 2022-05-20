# Implement algorithm to check if string has all unique characters. What if you cannot use additional data structures
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def has_unique(A):

    dct = {}

    for a in A:
        if a not in dct:
            dct[a]=1
        else:
            dct[a]+=1
            return False

    return True

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = numpy.array(list('356701'),dtype=numpy.int)
    #A = [3,2,4]

    res = has_unique(A)

    print(A)
    print(res)