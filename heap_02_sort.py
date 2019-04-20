# ----------------------------------------------------------------------------------------------------------------------
def heapify(A, i):
    N = len(A)
    left = (i+1)*2-1
    right = (i+1)*2+1-1

    argmax = i
    if left<N and A[left]>A[argmax]:
        argmax = left
    if right<N and A[right]>A[argmax]:
        argmax = right

    if argmax!=i:
        A[i],A[argmax] = A[argmax],A[i]
        heapify(A, argmax)

    return
# ----------------------------------------------------------------------------------------------------------------------
def build_heap(A):
    i=int(len(A)/2)
    while i>=0:
        heapify(A, i)
        i-=1

    return
# ----------------------------------------------------------------------------------------------------------------------
def heap_sort(A):

    build_heap(A)
    res = []
    for k in range(0,len(A)):
        res.append(A[0])
        A[0]=A[-1]
        del A[-1]
        heapify(A,0)
    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('4158345633')

    print(''.join(A))
    A=heap_sort(A)
    print(''.join(A))



