# Iterative 풀이 (스택을 사용)
# Time Complexity O(n) | Space Complexity O(h)
# 여기서 n은 노드의 갯수, h는 트리의 최대 높이

# def nodeDepths(root):
#     # Write your code here.
#     sum_of_depths = 0
#     stack = [{"node": root, "depth": 0}]
#
#     while len(stack) > 0:
#         node_info = stack.pop()
#         node, depth = node_info["node"], node_info["depth"]
#         if node is None:
#             continue
#         sum_of_depths += depth
#         stack.append({"node": node.left, "depth": depth + 1})
#         stack.append({"node": node.right, "depth": depth + 1})
#     return sum_of_depths

# 내풀이 및 재귀 풀이
# Time Complexity O(n) | Space Complexity O(h)
# 여기서 n은 노드의 갯수, h는 트리의 최대 높이

def node_depth_helper(node, depth):
    if node is None:
        return 0
    return depth + node_depth_helper(node.left, depth + 1) + node_depth_helper(node.right, depth + 1)


def nodeDepths(root):
    # Write your code here.
    return node_depth_helper(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
