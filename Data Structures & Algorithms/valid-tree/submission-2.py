class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #a tree has NO cycles, so we must perform another DFS to check if there is a cycle again
        visit = set()

        #we must build an adjecency list first 
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)  # undirected, so both directions

        def dfs(visit, node, parent_node):
            if node in visit:
                return False
            
            visit.add(node)
            print(visit)
            for nei in adj[node]:
                if nei == parent_node:
                    continue
                elif not dfs(visit, nei, node):
                    return False
            return True
        if len(edges) == 0:
            return True
        return_val = dfs(visit, edges[0][0], edges[0][0])
        if len(visit) == n and return_val:
            return True
        
        else:
            return False
