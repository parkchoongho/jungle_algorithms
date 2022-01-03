# This is an input class. Do not edit.
import sys


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 내 풀이
# def validate_bst_helper(node, min_value, max_value):
#     if min_value > node.value or node.value >= max_value:
#         return False
#     if node.left is not None:
#         if node.left.value >= node.value:
#             return False
#         else:
#             if validate_bst_helper(node.left, min_value, node.value):
#                 pass
#             else:
#                 return False
#     if node.right is not None:
#         if node.right.value < node.value:
#             return False
#         else:
#             if validate_bst_helper(node.right, node.value, max_value):
#                 pass
#             else:
#                 return False
#     return True
#
#
# def validate_bst(tree):
#     return validate_bst_helper(tree, -sys.maxsize - 1, sys.maxsize)

# algo expert 풀이
def validate_bst_helper(tree, max_value, min_value):
    if tree is None:
        return True
    if min_value > tree.value or tree.value >= max_value:
        return False
    return validate_bst_helper(tree.left, tree.value, min_value) and validate_bst_helper(tree.right, max_value, tree.value)


def validate_bst(tree):
    # Write your code here.
    return validate_bst_helper(tree, sys.maxsize, -sys.maxsize - 1)
