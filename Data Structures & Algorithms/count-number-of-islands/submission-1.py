class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS approach check all directions
        #base case: out of range, 0, or in visisted set
        #track num island in for loop, call dfs() when it ends then += 1 incremenet
        ROW, COL = len(grid), len(grid[0])

        #to help our direction checks
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            #base cases
            #no need for visisted will modify visited to 0 in place
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == "0":
                return 
            #this is how we mark as visited
            grid[r][c] = "0"
            #this is how we recurvicely call all directions should at the end be 0 for each island
            for nr, nc in directions:
                dfs(r + nr, c + nc)


        islands = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands



