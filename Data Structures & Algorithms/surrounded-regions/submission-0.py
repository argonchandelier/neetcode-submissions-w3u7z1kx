from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(coords, seen):
            r, c = coords
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                return False
            seen.add(coords)
            surrounded = True
            for dr, dc in ((0,1), (1,0), (0,-1), (-1,0)):
                r2, c2 = r+dr, c+dc
                coords2 = (r2, c2)
                if 0 <= r2 < m and 0 <= c2 < n and board[r2][c2] == 'O' and coords2 not in seen:
                    status = dfs(coords2, seen)
                    if not status:
                        surrounded = False
            return surrounded


        for r, row in enumerate(board):
            for c, tile in enumerate(row):
                if tile == 'O':
                    seen = set()
                    surrounded = dfs((r,c), seen)
                    if not surrounded:
                        continue
                    for r2, c2 in seen:
                        board[r2][c2] = 'X'
        
        
