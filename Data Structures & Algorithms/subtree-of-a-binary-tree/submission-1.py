# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root) #intialize the first root in subtree
        self.is_the_subtree = False
        #check is the subtree is the same
        def same_tree(treenode, subRoot):
            if not treenode and not subRoot:
                return True
            if (not treenode or not subRoot) or (treenode.val != subRoot.val):
                return False
            return same_tree(treenode.right, subRoot.right) and same_tree(treenode.left, subRoot.left)
        
        while q:
            processed_node = q.popleft()
            self.is_the_subtree = same_tree(processed_node, subRoot)
            if self.is_the_subtree:
                break
            if processed_node.right:
                q.append(processed_node.right)
            if processed_node.left:
                q.append(processed_node.left)
        return self.is_the_subtree
            


