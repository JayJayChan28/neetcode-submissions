"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #hash_map[node] = new_node_obj]
        #node.next --> find in hash_map[node] == new_node_obj
        #node.random --> find in hash_map[node] == new_node_obj

        #store node reference to the node 
        #create deep copy --> {node: deep_copy_node}
        deep_copy = {}
        dummy = head
        while dummy:
            if dummy not in deep_copy:
                deep_copy[dummy] = Node(dummy.val, None, None)
            dummy = dummy.next
        for node in deep_copy:
            #find .next of node
            deep_copy[node].next = deep_copy.get(node.next)

            #find .random of node
            deep_copy[node].random = deep_copy.get(node.random)
        if not head:
            return None
        return deep_copy[head]

        


