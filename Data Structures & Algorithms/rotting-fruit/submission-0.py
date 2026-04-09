class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = []
        nFresh = 0
        seen = set()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    rotten.append((r,c))
                    seen.add((r,c))
                elif val == 1:
                    nFresh += 1
        
        q = deque(rotten)
        def addToQ(coords):
            r, c = coords
            if 0 <= r < m and 0 <= c < n and coords not in seen and grid[r][c] == 1:
                nonlocal nFresh
                q.append(coords)
                seen.add(coords)
                nFresh -= 1

        mins = 0
        while q:
            mins += 1
            for size in range(len(q)):
                coords = q.popleft()
                r, c = coords
                for coords2 in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                    addToQ(coords2)
            if not q:
                mins -= 1
        
        if nFresh > 0:
            return -1
        return mins