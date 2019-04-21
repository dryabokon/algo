import numpy
# ----------------------------------------------------------------------------------------------------------------------
def find_elements_summup(A, S):
    dict={}
    for each in A:
        dict[S-each]=each

    for each in A:
        if each in dict and each!=S//2:
            print(each, dict[each])

    idx = numpy.where(A==S//2)[0]
    if len(idx)>=2:
        print(S//2,S//2)

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = numpy.array(list('55672'),dtype=numpy.int)

    find_elements_summup(A,10)