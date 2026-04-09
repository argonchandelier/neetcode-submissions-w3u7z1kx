from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        nodeGrid = [[None]*n for _ in range(m)]

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                node = Node(val)
                if r > 0:
                    unode = nodeGrid[r-1][c]
                    node.adj.append(unode)
                    unode.adj.append(node)
                if c > 0:
                    lnode = nodeGrid[r][c-1]
                    node.adj.append(lnode)
                    lnode.adj.append(node)
                nodeGrid[r][c] = node
        
        size = 0
        for r, row in enumerate(nodeGrid):
            for c, node in enumerate(row):
                if node.val == 0:
                    continue
                node.val = 0
                q = deque([node])
                count = 1
                while q:
                    cnode = q.popleft()
                    for adjNode in cnode.adj:
                        if adjNode.val == 0:
                            continue
                        adjNode.val = 0
                        count += 1
                        q.append(adjNode)
                size = max(size, count)
        
        return size