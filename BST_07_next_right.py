# ----------------------------------------------------------------------------------------------------------------------
from BST_01_build import BST_from_list
from BST_03_is_balanced import get_height
from BST_02_print import print_BST
# ----------------------------------------------------------------------------------------------------------------------
def put_nodes_into_levels(node,levels,cur_level=0):

    if node is None:return
    put_nodes_into_levels(node.L,levels,cur_level+1)
    levels[cur_level].append(node)
    put_nodes_into_levels(node.R,levels,cur_level+1)

    return
# ----------------------------------------------------------------------------------------------------------------------
def next_right(node):
    H = get_height(node)
    levels=[]
    for i in range(0,H):
        levels.append([])
    put_nodes_into_levels(root,levels,0)
    for i in range(0, H):
        lvl = levels[i]
        for j in range(0,len(lvl)-1):
            lvl[j]=lvl[j+1]

    return levels
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = list('jqpxldy')

    root = BST_from_list(A)
    print_BST(root)

    res = next_right(root)
    i=0


