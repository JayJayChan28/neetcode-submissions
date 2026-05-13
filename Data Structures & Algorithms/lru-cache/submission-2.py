class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.LRU, self.MRU = Node(0, 0), Node(0, 0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].val = value
            self.remove_node(self.hash_map[key])
            self.add_node(self.hash_map[key])
        else:
            new_node = Node(key, value)
            self.hash_map[key] = new_node
            self.add_node(new_node)
            self.size += 1
            if self.size > self.cap:
                lru_node = self.LRU.next
                self.remove_node(lru_node)
                del self.hash_map[lru_node.key]
                self.size -= 1


    
    #these are helpers to remove and add node
    
    def add_node(self, node_object):
        original_prev = self.MRU.prev
        self.MRU.prev = node_object
        node_object.next, node_object.prev = self.MRU, original_prev
        original_prev.next = node_object

    def remove_node(self, node_object):
        prev_node = node_object.prev
        next_node = node_object.next
        prev_node.next = next_node
        next_node.prev = prev_node
        

        
