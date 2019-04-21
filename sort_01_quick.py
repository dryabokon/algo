def partition(A, low=0, high=-1):
    p = low - 1
    pivot = A[high]
    for i in range(low, high):
        if pivot < A[i]:
            p+= 1
            A[p], A[i] = A[i], A[p]
    p += 1
    A[p], A[high] = A[high], A[p]
    return p
# ----------------------------------------------------------------------------------------------------------------------
def quick_sort(A,low,high):

    if low < high:
        p = partition(A, low, high)
        quick_sort(A, low, p - 1)
        quick_sort(A, p + 1, high)

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('76234524')
    print(''.join(A))

    #p = partition(A)
    #print(''.join(A[:p]), ''.join(A[p:]))

    quick_sort(A,0,len(A)-1)
    print(''.join(A))

