# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dsc_in_order(node, array):
    if node is None:
        return
    dsc_in_order(node.right, array)
    array.append(node.value)
    dsc_in_order(node.left, array)
    return array


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    # findKthLargestValueInBst(tree.right)
    array = dsc_in_order(tree, [])

    return array[k - 1]
