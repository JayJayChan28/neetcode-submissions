# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.stack = []

        def compute_val(root):
            while not root:
                return 
            
            compute_val(root.left)
            self.stack.append(root.val)
            compute_val(root.right)
        compute_val(root)
            
        return self.stack[k-1]



