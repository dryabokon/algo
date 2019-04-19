def selection_sort(A):

    for j in range(0,len(A)):
        best_value, best_idx = None,None
        for i in range(j,len(A)):
            if best_value is None or A[i]>best_value:
                best_value,best_idx = A[i],i

        A[best_idx], A[j] = A[j], A[best_idx]

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('2623447456234584')
    print(''.join(A))

    selection_sort(A)
    print(''.join(A))

