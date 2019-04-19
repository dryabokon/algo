def merge_sort(A):

    if len(A) < 2:
        return

    mid = len(A) // 2
    L = A[:mid].copy()
    R = A[mid:].copy()

    merge_sort(L)
    merge_sort(R)

    i,j,k = 0,0,0

    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('2623447456234584')
    print(''.join(A))

    merge_sort(A)
    print(''.join(A))

