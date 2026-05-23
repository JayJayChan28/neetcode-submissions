# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_same(q, p):
            if not q and not p:
                return True
            if ((p and not q) or (not p and q)) or (q.val != p.val):
                return False
            return is_same(q.left, p.left) and is_same(q.right, p.right)
        return is_same(q, p)

            
            