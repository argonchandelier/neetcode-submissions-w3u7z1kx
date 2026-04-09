class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        P = set()
        A = set()
        for r in range(m):
            P.add((r, 0))
            A.add((r, n-1))
        for c in range(n):
            P.add((0, c))
            A.add((m-1, c))
        
        qp = deque(list(P))
        qa = deque(list(A))

        def qLoop(q, goodSet):
            while q:
                cell = q.popleft()
                #if cell in goodSet:
                #    continue
                r, c = cell
                val = heights[r][c]
                for cell2 in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                    r2, c2 = cell2
                    if r2 < 0 or r2 >= m or c2 < 0 or c2 >= n:
                        continue
                    if cell2 in goodSet:
                        continue
                    val2 = heights[r2][c2]
                    if val2 >= val:
                        goodSet.add(cell2)
                        q.append(cell2)
            return goodSet
        
        P = qLoop(qp, P)
        A = qLoop(qa, A)
        both = P & A

        return [list(coords) for coords in both]


