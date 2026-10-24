class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ROW, COL = len(heights), len(heights[0])
        def dfs(r, c, set_type, prev_height):
            #base case
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r, c) in set_type or prev_height > heights[r][c]:
                return
            set_type.add((r, c))
            #if prev height is less than or equal to curr height
            for nr, nc in directions:
                dfs(r + nr, c + nc, set_type, heights[r][c])
            
            
        
        for r in range(ROW):
            dfs(r, 0, pacific_set, 0)
            dfs(r, COL - 1, atlantic_set, 0)
        for c in range(COL):
            dfs(0, c, pacific_set, 0)
            dfs(ROW - 1, c, atlantic_set, 0)
        res = []
        print(pacific_set)
        print(atlantic_set)
        for val in pacific_set:
            if val in atlantic_set:
                res.append(val)
        return res