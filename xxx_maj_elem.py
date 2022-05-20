def maj_elem(A):

    dct = {}
    for a in A:
        if a in dct:
            dct[a]+=1
        else:
            dct[a]=0

    k_max, v_max = A[0],dct[A[0]]


    for k,v in dct.items():
        if v>v_max:
            v_max =v
            k_max = k

    return k_max
# ----------------------------------------------------------------------------------------------------------------------
def maj_elem2(A):
    candidate, count = A[0], 0
    for a in A:
        if a == candidate:
            count += 1
        elif count == 0:
            candidate, count = a, 1
        else:
            count -= 1
    return candidate
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [2,2,1,1,1,2,2]

    res = maj_elem2(A)
    print(res)