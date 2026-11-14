# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent_insert = None
        if not root:
            return TreeNode(val)
        def dfs(node, parent, val):
            if not node:
                if parent.val >= val:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                return
            #if the parent is 
            if node.val >= val:
                dfs(node.left, node, val)
            else:
                dfs(node.right, node, val)
            
        dfs(root, parent_insert, val)
        return root