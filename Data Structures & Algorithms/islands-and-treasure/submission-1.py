class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #mulimodal BFS, in first pass add "0" to the qeueu
        # run bfs, while q in emtpy check all directions, if there is INF, then replace value with layer <-- this will represent 
        #use a visited set to ensure that we don't recomcuept esomething again 


        q = deque()
        ROW , COL = len(grid), len(grid[0])
        #add all chests to the queue
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
        #direction vector to help us check all directions
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        layer = 0

        vis = set()
        while q:
            layer += 1
            for _ in range(len(q)):
                #val will first contain the source "0" grid cell
                new_r, new_c = q.popleft()
                vis.add((new_r, new_c))
                for nr, nc in directions:
                    if new_r + nr < 0 or new_r + nr >= ROW or new_c + nc < 0 or new_c + nc >= COL:
                        continue
                    elif grid[new_r + nr][new_c + nc] == 2147483647 and (new_r + nr, new_c + nc) not in vis:
                        grid[new_r + nr][new_c + nc] = layer
                        q.append((new_r + nr, new_c + nc))
        

