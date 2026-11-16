class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(a, b):
            parent_a, parent_b = find(a), find(b)
            #if alreafy points to the same ref tree, means we unioned already
            if parent_a == parent_b:
                return False
            
            if rank[parent_a] > rank[parent_b]:
                parent[parent_b] = parent_a
                rank[parent_a] += rank[parent_b]
            else:
                parent[parent_a] = parent_b
                rank[parent_b] += rank[parent_a]

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]

            

