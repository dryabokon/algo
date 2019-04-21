# ----------------------------------------------------------------------------------------------------------------------
from BST_01_build import BST_from_list
from BST_02_print import print_BST
# ----------------------------------------------------------------------------------------------------------------------
def get_path(node,key):

    if node.key==key:
        return [key]
    elif key<node.key:
        return [node.key]+get_path(node.L, key)
    else:
        return [node.key] + get_path(node.R, key)

# ----------------------------------------------------------------------------------------------------------------------
def lowest_common_parent(root, key1, key2):
    path1 = get_path(root, key1)
    path2 = get_path(root, key2)
    i,j=0,0
    while (i<len(path1)) and (j<len(path2))and (path1[i]==path2[j]):
        i+=1
        j+=1

    return path1[i-1]
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = list('jqpxldy')

    root = BST_from_list(A)
    print_BST(root)
    print('--------')
    res = lowest_common_parent(root, 'q', 'x')
    print(res)

