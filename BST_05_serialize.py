# ----------------------------------------------------------------------------------------------------------------------
from BST_01_build import BST_from_list, Node
from BST_02_print import print_BST
# ----------------------------------------------------------------------------------------------------------------------
def BST_are_equal(node1,node2):

    is_none1 = (node1 is None)
    is_none2 = (node2 is None)

    if is_none1 and is_none2:
        return True

    if (is_none1 and not is_none2) or (not is_none1 and is_none2):
        return False

    if (node1.key != node2.key):
        return False
    else:
        return BST_are_equal(node1.L, node2.L) and BST_are_equal(node1.R, node2.R)

# ----------------------------------------------------------------------------------------------------------------------
def BST_serialize(node,sep='*'):

    res=[]
    if node is None:
        res=[sep]
        return res

    res.append(node.key)
    if node.L is not None:
        for each in BST_serialize(node.L):
            res.append(each)
    else:
        res.append(sep)

    if node.R is not None:
        for each in BST_serialize(node.R):
            res.append(each)
    else:
        res.append(sep)

    return res
# ----------------------------------------------------------------------------------------------------------------------
def BST_deserialize(list,sep='*'):

    if list[0]==sep:
        del (list[0])
        return None
    node = Node(list[0])
    del(list[0])

    node.L = BST_deserialize(list)
    node.R = BST_deserialize(list)


    return node
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = list('123twe45345')

    root1 = BST_from_list(A)

    serialized = BST_serialize(root1)
    print(''.join(serialized))

    root2 = BST_deserialize(serialized)

    res = BST_are_equal(root1,root1)
    print(res)

    print_BST(root1)
    print('-------------------')
    print_BST(root2)
