import numpy
#from heap_01_build import is_heap_topmax,build_heap
# ----------------------------------------------------------------------------------------------------------------------
def print_heap_as_tree_rotated(A,i=0,space=0):
    space_len = 4
    N = len(A)
    left  = 2 * (i + 1) - 1
    right = 2 * (i + 1) + 1 - 1

    space += space_len

    if (right< N):
        print_heap_as_tree_rotated(A, right, space)
    print()
    for s in range(space_len, space):print(end=" ")
    print(A[i])

    if (left< N):
        print_heap_as_tree_rotated(A, left, space)

    return
# ----------------------------------------------------------------------------------------------------------------------
def get_positions(i,L,ver_shift=0,hor_shift = 0):
    ver_pos, hor_pos = [],[]

    if i>L:
        return ver_pos, hor_pos

    left  = 2 * (i + 1) - 1
    right = 2 * (i + 1) + 1 - 1

    ver_pos += [ver_shift]
    hor_pos += [hor_shift]

    if (left<L):
        v,h = get_positions(left,L, ver_shift + 1, hor_shift - 1)
        ver_pos += v
        hor_pos += h
    if (right<L):
        v, h = get_positions(right,L, ver_shift + 1, hor_shift + 1)
        ver_pos += v
        hor_pos += h

    return ver_pos, hor_pos
# ----------------------------------------------------------------------------------------------------------------------
def print_heap_as_tree(heap, i=0, space=0):

    ver_pos, hor_pos = get_positions(0,len(heap), 0, 0)

    Wmin = min(hor_pos)
    Wmax = max(hor_pos)+1
    H = max(ver_pos)+1

    A = numpy.full((H,Wmax-Wmin),' ',dtype=numpy.chararray)
    for (row,col,value) in zip(ver_pos,hor_pos,heap):
        if A[row,col-Wmin]==' ':
            A[row,col-Wmin]=value
        else:
            A[row, col - Wmin] += ','+value

    for each in A:
        print('  '.join(each))

    print()
    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('1999')
    #res = is_heap(A)
    #print(res)
    build_heap(A)
    print_heap_as_tree(A)

    res = is_heap_topmax(A)
    print()
    print(''.join(A))

    print()
    print(res)





