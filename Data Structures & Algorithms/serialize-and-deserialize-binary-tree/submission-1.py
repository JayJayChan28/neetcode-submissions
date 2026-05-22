# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def helper_serilize(node):
            if not node:
                self.res.append("N")
                return 
            self.res.append(f"{node.val}")
            helper_serilize(node.left)
            helper_serilize(node.right)
        helper_serilize(root)
        self.res = ",".join(self.res)
        return self.res

    def deserialize(self, serialized):
        self.vals = serialized.split(",") #puts it back ito a list opposite of join
        self.index = 0
        def reconstruct():
            if self.vals[self.index] == "N":
                self.index += 1
                return None #base case
            node = TreeNode(int(self.vals[self.index]))
            self.index += 1
            node.left = reconstruct()
            node.right = reconstruct()
            return node
        return reconstruct()


