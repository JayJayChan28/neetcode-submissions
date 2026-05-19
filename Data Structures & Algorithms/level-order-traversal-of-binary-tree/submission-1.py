# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        nested_list = []
        num_pops = len(q)
        if not root:
            return []
        while q:
            level = []
            for _ in range(num_pops):
                processed_node = q.popleft()
                level.append(processed_node.val)
                left_child = processed_node.left
                right_child = processed_node.right
                if left_child:
                    q.append(left_child)
                if right_child:
                    q.append(right_child)
            num_pops = len(q)
            nested_list.append(level)
        return nested_list


