#Given two strings, write a method to decide if one is a permutation of the other.
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def is_permutation(A,B):

    dct = {}

    for a in A:
        if a not in dct:
            dct[a]=1
        else:
            dct[a]+=1

    for b in B:
        if b not in dct:
            return False
        else:
            dct[b]-=1

    for k,v in dct.items():
        if v!=0:
            return False


    return True

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = numpy.array(list('356702'),dtype=numpy.chararray)
    B = numpy.array(list('357601'),dtype=numpy.chararray)


    res = is_permutation(A,B)

    print(A,B)
    print(res)