from collections import deque
class Node:
    def __init__(self, val, adj=None):
        self.val = val
        self.adj = adj if adj is not None else []

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        nodeGrid = [[None]*n for _ in range(m)]
        startNodes = []
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                node = Node(val)
                if r > 0:
                    node2 = nodeGrid[r-1][c]
                    node2.adj.append(node)
                    node.adj.append(node2)
                if c > 0:
                    node2 = nodeGrid[r][c-1]
                    node2.adj.append(node)
                    node.adj.append(node2)
                nodeGrid[r][c] = node
                if val == 0:
                    startNodes.append(node)

        q = deque(startNodes)
        while q:
            cnode = q.popleft()
            v = cnode.val + 1
            for adjnode in cnode.adj:
                if adjnode.val <= v:
                    continue
                adjnode.val = v
                q.append(adjnode)
        
        for r, row in enumerate(nodeGrid):
            for c, node in enumerate(row):
                grid[r][c] = node.val
