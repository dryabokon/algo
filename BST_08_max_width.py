# ----------------------------------------------------------------------------------------------------------------------
from BST_01_build import BST_from_list
from BST_03_is_balanced import get_height
from BST_02_print import print_BST
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def traverse_for_depth_pos(node,depth,pos):

    if node.L is None and node.R is None:
        return [depth],[pos]
    levels,positions = [],[]
    if node.L is not None:
        levels,positions = traverse_for_depth_pos(node.L,depth+1,2*pos)

    levels.append(depth)
    positions.append(pos)

    if node.R is not None:
        l,p= traverse_for_depth_pos(node.R,depth+1,2*pos+1)
        levels+=l
        positions+=p

    return levels, positions
# ----------------------------------------------------------------------------------------------------------------------
def max_width(root):

    level,pos = traverse_for_depth_pos(root,0,0)
    pos = numpy.array(pos)
    level = numpy.array(level)
    max_depth = 0
    for each in set(level):
        idx = numpy.where(level==each)
        d = numpy.max(pos[idx])-numpy.min(pos[idx])
        max_depth = max(max_depth,d)

    return max_depth
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = list('jqpxldy')

    #root = BST_from_list(A)
    #res = max_width(root)
    #print(res)

    B=u'sdfsfsdf'
    BB = list(B.encode('utf-8'))
    C = [chr(each) for each in BB]
    D = ''.join(C)
    print(D)



