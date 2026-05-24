# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def calculate_good(node, max_val):
            if not node:
                return 0
            if node.val >= max_val:
                self.res += 1
            max_val = max(max_val, node.val)
            calculate_good(node.left, max_val)
            calculate_good(node.right, max_val)
        calculate_good(root, float("-inf"))
        return self.res



            
            