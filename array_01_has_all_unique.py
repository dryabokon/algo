# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures
# ----------------------------------------------------------------------------------------------------------------------
# - Compare every character of the string to every other character of the string. This will take 0( n2) time and 0(1) space.
# - If we are allowed to modify the input string, we could sort the string in O(n log(n)) time and then linearly check
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def has_all_unique(A):

    flag255 = numpy.zeros(255)
    res = True

    for a in A:
        i = ord(a)
        if flag255[i]>0:
            res = False
            break
        else:
            flag255[i]+=1

    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = numpy.array(list('3t456'),dtype=numpy.chararray)
    res = has_all_unique(A)
    print(res)