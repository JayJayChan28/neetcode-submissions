# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        num_iter = len(q)
        if not root:
            return []
        while q:
            right_side_val = None
            for _ in range(num_iter):
                processed_node = q.popleft()
                if processed_node.left:
                    q.append(processed_node.left)
                if processed_node.right:
                    q.append(processed_node.right)
            num_iter = len(q)
            right_side_val = processed_node 
            res.append(right_side_val.val)
        return res

