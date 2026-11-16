class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        #each is its own tree initally with one
        rank = [1] * n 

        #parent = [0, 1, 2, 3, 4]
        #.         0, 1, 2, 3, 4
        def find(node):
            #if node is not parent of itself
            while parent[node] != node:
                #reassign current nodes grandparent is node the parent
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            #this should be the reference node now
            return node
        
        def union(n1, n2):
            n1_ref, n2_ref = find(n1), find(n2)
            #if connected, no need to connect
            if n1_ref == n2_ref:
                return False
            
            #find whch one is bigger this case is n1 is bigger n2 becauses the child
            if rank[n1_ref] > rank[n2_ref]:
                parent[n2_ref] = n1_ref
                #increase the total by the rank of the smaller n2 tree
                rank[n1_ref] += rank[n2_ref]
            else:
                parent[n1_ref] = n2_ref
                #increase the total by the rank of the smaller n2 tree
                rank[n2_ref] += rank[n1_ref]
            return True

        num_union = 0
        for a, b in edges:
            #meaning if a union of sucessfull
            if union(a, b):
                num_union += 1
        
        #this is a formual for num of components
        return n - num_union

            


                 

