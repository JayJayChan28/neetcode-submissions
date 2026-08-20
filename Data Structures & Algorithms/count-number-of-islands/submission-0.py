class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs approach, vis, deque, 
        #check all directions --> mark directions that we visisted my making it "0"
        #if grid[r][c] == "1" then we search deeper 

        #up down left right
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        islands = 0

        #get row + col index
        ROW, COL = len(grid), len(grid[0])
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nc, nr = col + dc, row + dr
                    if (nr < 0 or nc < 0 or 
                    nr >= ROW or 
                    nc >= COL or grid[nr][nc] == "0"):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
                
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
                    
        return islands

