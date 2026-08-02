class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(sub, close_par, open_par):
            #base case
            if len(sub) == 2*n:
                results = "".join(sub)
                res.append(results)
                return 
            #contraints
            
            if close_par < open_par or open_par > n:
                sub.append(")")
                dfs(sub, close_par + 1, open_par)
                sub.pop()
            if open_par < n:
                sub.append("(")
                dfs(sub, close_par, open_par + 1)
                sub.pop()
        
        dfs([], 0, 0)
        
        return res
        
