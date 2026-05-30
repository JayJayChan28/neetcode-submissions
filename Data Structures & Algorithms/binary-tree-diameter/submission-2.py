# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #set global var max_path
        #use helper function to run dfs postorder traversal
        #return the max(left, right) + 1

        self.max_path = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_path  = max(self.max_path, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.max_path