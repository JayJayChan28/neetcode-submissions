class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_fruits = 0
        total_rotted_fruits = 0

        q = deque()
        vis = set()
        ROW, COL = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        #see total fruits, rotted fruits + add rotted into queue
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 or grid[r][c] == 2:
                    total_fruits += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    total_rotted_fruits += 1
        
        rotted_fruits = total_rotted_fruits
        minutes = 0
        while q:
            is_rotted = False
            #process layer by layer
            for _ in range(len(q)):
                new_r, new_c = q.popleft()
                vis.add((new_r, new_c))
                for nr, nc in directions:
                    if (new_r + nr, new_c + nc) in vis or new_r + nr < 0 or new_r + nr >= ROW or new_c + nc < 0 or new_c + nc >= COL:
                        continue
                    elif grid[new_r + nr][new_c + nc] == 1:
                        rotted_fruits += 1
                        grid[new_r + nr][new_c + nc] = 2
                        q.append((new_r + nr, new_c + nc))
                        is_rotted = True
            if is_rotted:
                minutes += 1
        if rotted_fruits == total_fruits:
            return minutes
        else:
            return -1

                    



            

                



            