# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildthetree(preorder, inorder):
            if not preorder or not inorder:
                return
            root = preorder[0]

            mid = inorder.index(root)
            new_node = TreeNode(preorder[0])
            new_node.left = buildthetree(preorder[1:mid + 1], inorder[:mid])
            new_node.right = buildthetree(preorder[mid + 1:], inorder[mid + 1:])
            return new_node
        return buildthetree(preorder, inorder)
