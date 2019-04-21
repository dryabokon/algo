import numpy
# ----------------------------------------------------------------------------------------------------------------------
def get_all_permutations(array):

    # 1234
    # 1243
    # 1324
    # 1342
    # 1432
    # 1423
    if array.shape[0]==1:
        return numpy.array([array[0]])

    result =[]
    for i in range(0, array.shape[0]):
        sub_array=numpy.delete(array,i)
        sub_perm = get_all_permutations(sub_array)
        for each in sub_perm:
            r =numpy.insert(numpy.array(each), 0, array[i])
            result.append(r)

    return result
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = numpy.array(list('ABAD'))
    res = get_all_permutations(A)
    for each in res:
        print(each)

