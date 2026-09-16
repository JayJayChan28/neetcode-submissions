"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #create hash of node to neighboors
        # 1--n so we can just set the hash val to 1 - n w/ eighboors o them 

        #use dfs approach 
        hash_map = {}
        def dfs(n):
            #base case if node alr exsists, just return the value of that 
            if n in hash_map:
                return hash_map[n]
            
            #if node doesn't exsist yet in hash_map, lets create a node
            new_node = Node(n.val)
            hash_map[n] = new_node
            for nei in n.neighbors: 
                hash_map[n].neighbors.append(dfs(nei))
            
            return new_node
        
        if node:
            return dfs(node)

