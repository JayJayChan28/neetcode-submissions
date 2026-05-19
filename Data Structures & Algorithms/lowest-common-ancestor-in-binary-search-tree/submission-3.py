# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack_p = self.find_node(root, p)
        stack_q = self.find_node(root, q)

        for i in stack_q:
            print(i.val)
        
        for i in stack_p:
            print(i.val)
        
        while len(stack_q) != len(stack_p):
            if len(stack_q) > len(stack_p):
                # print(stack_q[-1].val)
                stack_q.pop()
            if len(stack_p) > len(stack_q):
                # print(stack_p[-1].val)
                stack_p.pop()
        while stack_p[-1].val != stack_q[-1].val:
            stack_p.pop()
            stack_q.pop()
        return stack_p[-1]
            






    def find_node(self, root, node):
        curr = root
        stack = []
        while curr.val != node.val:
            stack.append(curr)
            if curr.val < node.val:
                curr = curr.right
            elif curr.val > node.val:
                curr = curr.left
        stack.append(node)

        
        return stack
    
    

                
            
        