# 큐를 사용한 풀이법
# Time Complexity - O(N) | Space Complexity - O(d)
# def invertBinaryTree(tree):
#     # Write your code here.
#     queue = [tree]
#     while len(queue) > 0:
#         node = queue.pop(0)
#         if node is None:
#             continue
#         node.left, node.right = node.right, node.left
#         queue.append(node.left)
#         queue.append(node.right)

# 내 풀이
# 재귀 풀이법
# Time Complexity - O(N) | Space Complexity - O(d)
def invert_binary_tree_helper(node):
    if node is None:
        return
    # 조금 더 파이썬스러운 코드
    node.left, node.right = node.right, node.left

    invert_binary_tree_helper(node.left)
    invert_binary_tree_helper(node.right)


def invertBinaryTree(tree):
    # Write your code here.
    invert_binary_tree_helper(tree)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
