import numpy
# ----------------------------------------------------------------------------------------------------------------------
from BST_01_build import BST_from_list, inorder_trversal
# ----------------------------------------------------------------------------------------------------------------------
def get_positions(node,ver_shift=0,hor_shift = 0):
    ver_pos, hor_pos = [],[]

    if node is None:
        return ver_pos, hor_pos

    v,h = get_positions(node.L, ver_shift + 1, hor_shift - 1)
    ver_pos += v
    hor_pos += h
    ver_pos += [ver_shift]
    hor_pos += [hor_shift]
    v, h = get_positions(node.R, ver_shift + 1, hor_shift + 1)
    ver_pos += v
    hor_pos += h

    return ver_pos, hor_pos
# ----------------------------------------------------------------------------------------------------------------------
def print_BST(node, spaces=0):

    ver_pos, hor_pos = get_positions(node,0,0)
    values = inorder_trversal(node)
    Wmin = numpy.min(hor_pos)
    Wmax = numpy.max(hor_pos)+1
    H = numpy.max(ver_pos)+1

    A = numpy.full((H,Wmax-Wmin),' ',dtype=numpy.chararray)
    for (row,col,value) in zip(ver_pos,hor_pos,values):
        if A[row,col-Wmin]==' ':
            A[row,col-Wmin]=value
        else:
            A[row, col - Wmin] += ','+value

    for each in A:print('  '.join(each))


    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('12345345')
    root = BST_from_list(A)
    print_BST(root)