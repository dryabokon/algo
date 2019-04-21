# ----------------------------------------------------------------------------------------------------------------------
class Node():
    def __init__(self,key):
        self.key = key
        self.L = None
        self.R = None
        self.value = None

# ----------------------------------------------------------------------------------------------------------------------
def BST_insert(root, node):

    if root.key < node.key:
        if root.R is None:
            root.R = node
        else:
            BST_insert(root.R,node)
    else:
        if root.L is None:
            root.L = node
        else:
            BST_insert(root.L,node)

    return
# ----------------------------------------------------------------------------------------------------------------------
def BST_delete(node, key):
    #geeksforgeeks.org/binary-search-tree-set-2-delete/
    if node is None:
        return node

    if key < node.key and node.L is not None:
        node.L= BST_delete(node.L, key)

    elif key > node.key and node.R is not None:
        node.R = BST_delete(node.R, key)

    else: # delete the node

        if node.L is None:
            return node.R

        elif node.R is None:
            return node.L

        smalest_leaf = get_smalest_leaf(node.R)
        node.key = smalest_leaf.key
        node.R = BST_delete(node.R, smalest_leaf.key)

    return node
# ----------------------------------------------------------------------------------------------------------------------
def is_BST(node):

    res = True

    if node.L is not None:
        res = res and node.L.key <= node.key
        res = res and is_BST(node.L)

    if node.R is not None:
        res = res and node.key <= node.R.key
        res = res and is_BST(node.R)

    return res
# ----------------------------------------------------------------------------------------------------------------------
def BST_from_list(A):

    root = Node(A[0])
    for each in A[1:]:
        BST_insert(root,Node(each))

    return root
# ----------------------------------------------------------------------------------------------------------------------
def BST_from_list_ordered(ordered_list):
    L = len(ordered_list)
    if L==0:
        return None

    mid = int(L/2)
    root = Node(ordered_list[mid])
    root.L = BST_from_list_ordered(ordered_list[:mid])
    root.R= BST_from_list_ordered(ordered_list[mid + 1:])
    return root
# ----------------------------------------------------------------------------------------------------------------------
def inorder_trversal(node):

    res = []
    if node is None:
        return res

    res = inorder_trversal(node.L)
    res.append(node.key)
    for each in inorder_trversal(node.R):
        res.append(each)

    return res
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = list('12345345')
    BST_from_list(A)