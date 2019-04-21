# ----------------------------------------------------------------------------------------------------------------------
from sort_01_quick import partition
# ----------------------------------------------------------------------------------------------------------------------
def best_kth_element_quickselect(A, k):

    if k>len(A) or k<=0:
        return []

    if len(A)==1 and k==1:
        return A[0]

    p = partition(A, 0, len(A)-1) #A[:p] > A[p:]

    if p == k-1:
        return A[p]

    elif p > k-1:
        return best_kth_element_quickselect(A[:p], k)
    else:
        return best_kth_element_quickselect(A[p+1:], k-p-1)
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = list('12356sdklfhghab23456784')
    print(''.join(A))
    B = A.copy()
    B.sort(reverse=True)
    print(''.join(B))

    res = [best_kth_element_quickselect(A, k) for k in range(1,len(A)+1)]
    print(''.join(res))

