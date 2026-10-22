# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #conduct a BFS approach to solution 
        #use queue strucutre, last pop is the right side view
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            for _ in range(size):
                value = q.popleft()
                if value.left:
                    q.append(value.left)
                if value.right:
                    q.append(value.right)
            
            res.append(value.val)

        return res



