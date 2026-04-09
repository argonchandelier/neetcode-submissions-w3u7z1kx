from collections import deque

class Node:
    def __init__(self, val, left=None, right=None, up=None, down=None):
        self.val = val

        self.left = left
        self.right = right
        self.up = up
        self.down = down

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        nodeGrid = [[None]*n for _ in range(m)]

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                newNode = Node(int(val))
                if r > 0:
                    uNode = nodeGrid[r-1][c]
                    newNode.up = uNode
                    uNode.down = newNode
                if c > 0:
                    lNode = nodeGrid[r][c-1]
                    newNode.left = lNode
                    lNode.right = newNode
                nodeGrid[r][c] = newNode
        
        count = 0
        for r, row in enumerate(nodeGrid):
            for c, node in enumerate(row):
                if node.val == 0:
                    continue
                count += 1
                node.val = 0
                q = deque([node])
                while q:
                    cnode = q.popleft()
                    for newNode in [cnode.right, cnode.down, cnode.left, cnode.up]:
                        if newNode is None:
                            continue
                        if newNode.val == 0:
                            continue
                        newNode.val = 0
                        q.append(newNode)
        
        return count

                
