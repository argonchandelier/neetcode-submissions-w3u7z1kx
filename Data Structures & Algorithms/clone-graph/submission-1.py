"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        root = Node(node.val)
        '''
        q = deque([node])
        while q:
            cnode = q.popleft()
            for adjNode in cnode.neighbors:
                q.append(adjNode)
                newNode = Node(adjNode.val)
        '''
        seen = {node: root}
        def dfs(parent, cloneParent):
            for adjNode in parent.neighbors:
                if adjNode in seen:
                    newNode = seen[adjNode]
                    #print(f"appending {newNode.val} to {parent.val}")
                    if newNode not in cloneParent.neighbors:
                        cloneParent.neighbors.append(newNode)
                    continue
                newNode = Node(adjNode.val, neighbors = [cloneParent])
                cloneParent.neighbors.append(newNode)
                seen[adjNode] = newNode
                dfs(adjNode, newNode)

        dfs(node, root)
            
        return root
