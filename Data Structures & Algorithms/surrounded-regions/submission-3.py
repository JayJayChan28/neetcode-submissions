class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or board[r][c] != "O":
                return
            board[r][c] = "T"   # safe: connected to border
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # 1. only start from border cells
        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or r == ROW - 1 or c == 0 or c == COL - 1) and board[r][c] == "O":
                    dfs(r, c)

        # 2. leftover O = surrounded -> X, T = safe -> O
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"