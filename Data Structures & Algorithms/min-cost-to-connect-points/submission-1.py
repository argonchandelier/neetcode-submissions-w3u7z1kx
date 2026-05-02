import heapq
from bisect import bisect_left

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        edges = [] # [(cost, n1, n2), ...]
        for i, (x1, y1) in enumerate(points):
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x2-x1)+abs(y2-y1)
                heapq.heappush(edges, (cost, i, j))
        
        connected = [i for i in range(n)]
        connections = [{i} for i in range(n)]
        ci = 1
        res = 0
        while ci < n:
            cost, n1, n2 = heapq.heappop(edges)
            c1, c2 = connected[n1], connected[n2]
            if c1 == c2:
                continue
            mn = min(c1, c2)
            mx = max(c1, c2)
            connections[mn].update(connections[mx])
            for nd in connections[mn]:
                connected[nd] = mn
            res += cost
            while ci < n and connected[ci] == 0:
                ci += 1
        
        return res


