def bubble_sort(A):

    for top in range(0,len(A)-1):
        for bubble in reversed(range(top+1,len(A))):
            if A[bubble-1]<A[bubble]:
                A[bubble],A[bubble - 1] =A[bubble-1],A[bubble]
    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('2623447456234584')
    print(''.join(A))

    bubble_sort(A)
    print(''.join(A))

