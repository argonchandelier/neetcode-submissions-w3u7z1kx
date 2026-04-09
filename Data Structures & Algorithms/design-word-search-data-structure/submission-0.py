class Node:
    def __init__(self, char=""):
        self.char = char
        self.children = {}

    def addChild(self, char=""):
        newNode = Node(char)
        self.children[char] = newNode
        return newNode
    
    def isChild(self, char=""):
        return char in self.children
    
    def getChild(self, char=""):
        return self.children[char]

class WordDictionary:
    def __init__(self):
        self.headNode = Node()
        self.headNode.addChild()

        self.word = ""
        self.n = 0

    def addWord(self, word: str) -> None:
        curNode = self.headNode
        for char in word:
            exists = curNode.isChild(char)
            if not exists:
                newNode = curNode.addChild(char)
            curNode = curNode.getChild(char)
        if not exists:
            curNode.addChild()

    def search(self, word: str) -> bool:
        self.word = word
        self.n = len(self.word)
        return self.splitSearch(0, self.headNode)
    
    def splitSearch(self, i, curNode):
        if i == self.n:
            return curNode.isChild()

        char = self.word[i]
        if char == '.':
            for key in curNode.children:
                exists = self.splitSearch(i+1, curNode.getChild(key))
                if exists:
                    return True
            return False
        else:
            exists = curNode.isChild(char)
            if not exists:
                return False
            nextNode = curNode.getChild(char)
            return self.splitSearch(i+1, nextNode)





        
