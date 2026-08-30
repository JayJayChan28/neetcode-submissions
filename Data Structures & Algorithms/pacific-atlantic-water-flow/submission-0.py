class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific_set, atlantic_set = set(), set()
        ROW, COL = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, curr_height, type_set, vis):
            if r < 0 or r >= ROW or c < 0 or c >= COL or heights[r][c] < curr_height or (r, c) in vis:
                return 
            elif heights[r][c] >= curr_height:
                type_set.add((r, c))
            vis.add((r, c))
            for nr, nc in directions:
                dfs(r + nr, c + nc, heights[r][c], type_set, vis)
        
        #lets calculate for the pacific first
        #pacific needs 0,0 --> 0, len(col) and from 0,0 --> r < 0, 0
        pacific_vis = set()
        for c in range(COL):
            dfs(0, c, heights[0][c], pacific_set, pacific_vis)
        for r in range(ROW):
            dfs(r, 0, heights[r][0], pacific_set, pacific_vis)
        atlantic_vis = set()
        for c in range(COL):
            dfs(ROW - 1, c, heights[ROW - 1][c], atlantic_set, atlantic_vis)
        for r in range(ROW):
            dfs(r, COL - 1, heights[r][COL - 1], atlantic_set, atlantic_vis)

        for r, c in pacific_set:
            if (r, c) in atlantic_set:
                res.append([r, c])
        return res