# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def max_height(node):
            if not node:
                return 0
            left_node_depth = max_height(node.left)
            right_node_depth = max_height(node.right)

            if abs(left_node_depth - right_node_depth) > 1:
                self.result = False

            return 1 + max(left_node_depth, right_node_depth)
        max_height(root)
        return self.result
        