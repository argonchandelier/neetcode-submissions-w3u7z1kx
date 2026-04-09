class Node:
    def __init__(self, char=" "):
        self.char = char
        self.children = {} # char: node
    
    def addChild(self, char=" "):
        childNode = Node(char)
        self.children[char] = childNode
        return childNode
    
    def isChild(self, char=" "):
        return char in self.children
    
    def getChild(self, char):
        return self.children[char]

class PrefixTree:

    def __init__(self):
        self.headNode = Node()
        self.headNode.addChild()

    def insert(self, word: str) -> None:
        frontier = False
        curNode = self.headNode
        for char in word:
            frontier = not curNode.isChild(char)
            if frontier:
                newNode = curNode.addChild(char)
                curNode = newNode
            else:
                curNode = curNode.getChild(char)
        if not curNode.isChild():
            curNode.addChild()

    def search(self, word: str) -> bool:
        curNode = self.headNode
        for char in word:
            exists = curNode.isChild(char)
            if not exists:
                return False
            curNode = curNode.getChild(char)
        return curNode.isChild()

    def startsWith(self, prefix: str) -> bool:
        curNode = self.headNode
        for char in prefix:
            exists = curNode.isChild(char)
            if not exists:
                return False
            curNode = curNode.getChild(char)
        return True
        