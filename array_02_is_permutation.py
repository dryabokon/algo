# Given two strings, write a method to decide if one is a permutation of the other
# ----------------------------------------------------------------------------------------------------------------------
import numpy
from collections import Counter
# ----------------------------------------------------------------------------------------------------------------------
def is_permutation(A, B):


    flag255 = numpy.zeros(255)
    for a in A:
        i = ord(a)
        flag255[i]+=1

    for b in B:
        i = ord(b)
        flag255[i]-=1

    res = (numpy.count_nonzero(flag255)==0)

    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = numpy.array(list('3t45668'),dtype=numpy.chararray)
    B = numpy.array(list('3t4665'), dtype=numpy.chararray)
    res = is_permutation(A,B)
    print(res)