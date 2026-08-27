class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs appraoach, to return of the area of each island when we hit a "1"
        #if 1 then we reeuce deeper 


        ROW,COL = len(grid), len(grid[0])

        
        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area

            
            

            
            

