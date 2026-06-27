# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr_node = root
        height = 0

        while curr_node:
            if min(p.val, q.val) <= curr_node.val <= max(q.val, p.val):
                return curr_node
            elif curr_node.val <= min(p.val, q.val):
                curr_node = curr_node.right
            elif curr_node.val >= max(q.val, p.val):
                 curr_node = curr_node.left
            height += 1
        
