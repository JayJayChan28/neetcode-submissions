class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #conditions:
        #1: if num open > n --> have to insert a close parenthesis
        #2: # close < # open --> then we can insert a close paren on backtrack
        #base case: and if close + open == 2 times n --> we hit base case

        res = []

        def dfs(sub, num_open, num_close):
            if num_open + num_close == (n*2):
                res.append("".join(sub.copy()))
            if num_open < n:
                sub.append("(")
                dfs(sub, num_open + 1, num_close)
                sub.pop()
            if num_open > n or num_close < num_open:
                sub.append(")")
                dfs(sub, num_open, num_close + 1)
                sub.pop()
        dfs([], 0, 0)
        return res
            
            
