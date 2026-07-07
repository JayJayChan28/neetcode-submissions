# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_bst = True
        def val_bounds(node, lower, upper):
            #we hit out base case that means we return true, this node is valid
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return val_bounds(node.left, lower, node.val) and val_bounds(node.right, node.val, upper)
        return val_bounds(root, float("-inf"), float("inf"))