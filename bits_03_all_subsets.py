# ----------------------------------------------------------------------------------------------------------------------
#get all subsets of a set.
def get_all_subsets(A):
    import numpy
    A = numpy.array(A)
    N=len(A)
    res = [[]]
    idxs = []

    for i in range(0,2**N):
        idxs.append(([(i>>b)&1 for b in range(0,N)]))


    for idx in idxs:
        ii = [i for i,ii in enumerate(idx) if ii>0]
        if len(ii)>0:
            res.append(A[[ii]])
    return res

# ----------------------------------------------------------------------------------------------------------------------
def get_all_subsets2(A):
    result = [[]]
    for a in A:
        tmp_res = [r + [a] for r in result]
        result += tmp_res
    return result
# ----------------------------------------------------------------------------------------------------------------------
def get_all_subsets_no_dups(A, path=None, result=None):


    result.append(path)
    for i in range(len(A)):
        if i > 0 and A[i] == A[i - 1]:
            continue
        result = get_all_subsets_no_dups(A[i+1:], path + [A[i]], result)

    return result
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [1,2,3]


    res = get_all_subsets_no_dups(A)
    for r in res:
        print(r)
