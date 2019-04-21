# ----------------------------------------------------------------------------------------------------------------------
from BST_01_build import BST_from_list, BST_from_list_ordered, is_BST
# ----------------------------------------------------------------------------------------------------------------------
def get_height(node):
    if node is None:
        return 0
    return max(get_height(node.L), get_height(node.R)) + 1
# ----------------------------------------------------------------------------------------------------------------------
def is_BST_balanced(node):
    if node is None:
        return True

    return is_BST(node) and abs(get_height(node.L)-get_height(node.R))<= 1 and is_BST_balanced(node.L) and is_BST_balanced(node.R)
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('19345345')
    root = BST_from_list(A)
    print(is_BST_balanced(root))

    A.sort()
    root = BST_from_list_ordered(A)
    print(is_BST_balanced(root))

