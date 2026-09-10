class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs algo, convert 1's to 0's --> for each "1" that we find while iterating through the graph

        ROW, COL = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
            for nr, nc in directions:
                dfs(nr + r, nc + c)            
        num_islands = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)
        return num_islands