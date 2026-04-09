class Node:
    def __init__(self, val, up=None, left=None, right=None, down=None):
        self.val = val
        self.up = up
        self.left = left
        self.right = right
        self.down = down
    
    def isMatch(self, val):
        return val == self.val

class Solution:
    def initNodes(self, board):
        m = len(board)
        n = len(board[0])
        nodes = []
        for i in range(m):
            for j in range(n):
                val = board[i][j]
                node = Node(val)

                if 0 <= i-1 < m:
                    upNode = nodes[(i-1)*n+j]
                    node.up = upNode
                    upNode.down = node
                if 0 <= j-1 < n:
                    leftNode = nodes[i*n+j-1]
                    node.left = leftNode
                    leftNode.right = node
                
                nodes.append(node)
        
        return nodes
    
    def traverse(self, i, node, prev):
        if not node or not node.isMatch(self.word[i]):
            return False
        if i == self.n-1:
            return True
        
        for nextNode in [node.up, node.left, node.right, node.down]:
            if nextNode in prev:
                continue
            isIn = self.traverse(i+1, nextNode, prev + [node])
            if isIn:
                return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        nodes = self.initNodes(board)
        self.word = word
        self.n = len(word)

        for node in nodes:
            found = self.traverse(0, node, [])
            if found:
                return True
        return False
        