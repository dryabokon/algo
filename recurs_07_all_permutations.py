import numpy
# ----------------------------------------------------------------------------------------------------------------------
def get_all_permutations(A):

    # 1234
    # 1243
    # 1324
    # 1342
    # 1432
    # 1423
    if len(A)==1:
        return [[A[0]]]

    result =[]
    for i in range(0, len(A)):
        sub_array = [each for each in A]
        del(sub_array[i])
        sub_perm = get_all_permutations(sub_array)
        for each in sub_perm:
            r =[A[i]] + each
            result.append(r)

    return result
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = list('1234')
    res = get_all_permutations(A)
    for each in res:
        print(''.join(each))

