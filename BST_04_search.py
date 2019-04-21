# ----------------------------------------------------------------------------------------------------------------------
from BST_01_build import BST_from_list
# ----------------------------------------------------------------------------------------------------------------------
def BST_search(node,key):

    res = None

    if node.key == key:
        return key

    if key<= node.key and node.L is not None:
        res = BST_search(node.L,key)

    if res is None and node.key <= key and node.R is not None:
        res = BST_search(node.R,key)

    return res
# ----------------------------------------------------------------------------------------------------------------------
def BST_search_min(node):
    if node.L is None:
        return node.key

    while (node.L is not None):
        return BST_search_min(node.L)

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('12345345')
    root = BST_from_list(A)
    res = BST_search(root,'4')
    print(res)


