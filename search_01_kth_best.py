import heap_01_build as heap
# ----------------------------------------------------------------------------------------------------------------------
def best_kth_element(A, k):

    H = A.copy()
    heap.build_heap(H)

    res=[]
    for i in range(0,k):
        res = H[0]
        H[0] = H[-1]
        del(H[-1])
        heap.heapify(H, 0)

    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('765123')
    print(''.join(A))
    res = best_kth_element(A,1)
    print(res)
