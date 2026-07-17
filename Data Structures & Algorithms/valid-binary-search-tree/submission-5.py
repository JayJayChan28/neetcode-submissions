# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#use property of BST 
# store 3 params, min bound, max bound, and then curr node
#serach left, update max_bound <--- everyting left must be smaller
#serach right, update min_bound <-- everytrihg right but be larer
#valvcaulte this in a nested fucntion 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum = float('-inf')
        maximum = float('inf')
        def is_bst(node, min_bound, max_bound):
            if not node:
                return True
            print(min_bound)
            print(node.val)
            print(max_bound)
            if not min_bound < node.val < max_bound:
                return False
            return is_bst(node.left, min_bound, node.val) & is_bst(node.right, node.val, max_bound)
        return is_bst(root, minimum, maximum)
        