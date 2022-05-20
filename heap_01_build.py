from heap_04_print import print_heap_as_tree
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
        print_heap_as_tree(A)
        heapify(A, i)
        i-=1

    return
# ----------------------------------------------------------------------------------------------------------------------
def get_max(maxheap):
    return maxheap[0]
# ----------------------------------------------------------------------------------------------------------------------
def heap_Kth_max(maxheap,K):
    H = maxheap.copy()
    res = []
    for k in range(0,K):
        res = H[0]
        H[0]=H[-1]
        H.pop(1)
        heapify(H, 0)

    return res
# ----------------------------------------------------------------------------------------------------------------------
def heap_search(A,value):
    for i in range(0,len(A)):
        if A[i]==value:
            return i
    return None
# ----------------------------------------------------------------------------------------------------------------------
def heap_insert(A,value):

    A.insert(0,value)
    heapify(A, 0)
    return
# ----------------------------------------------------------------------------------------------------------------------
def heap_delete(A,value):

    i = heap_search(A,value)
    if i is not None:
        A[i]=A[-1]
        del A[-1]
        heapify(A, i)

    return
# ----------------------------------------------------------------------------------------------------------------------
def is_heap_topmax(A,i=0):

    left  = (i+1)*2-1
    right = (i+1)*2+1-1


    if left < len(A):
        is_leftheap = (A[i] > A[left]) and is_heap_topmax(A,left)
    else:
        is_leftheap = True

    if right < len(A):
        is_rightheap  = (A[i] > A[right]) and is_heap_topmax(A,right)
    else:
        is_rightheap = True

    return is_leftheap and is_rightheap
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('4158345633')

    build_heap(A)
    heap_delete(A,1)

