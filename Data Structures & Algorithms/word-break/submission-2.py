class Node:
    def __init__(self, char, children=None):
        self.char = char
        self.children = {} if children is None else children # Maps chars to next node
        self.end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wds = set(wordDict)
        n = len(s)
        m = len(wordDict)
        t = 0
        wdLens = [0]*m
        for i, word in enumerate(wordDict):
            t = max(t, len(word))
            wdLens[i] = len(word)
        
        nodeMap = {}
        curNodes = [None]*m
        for i, word in enumerate(wordDict):
            c0 = word[0]
            if c0 not in nodeMap:
                newNode = Node(c0)
                nodeMap[c0] = newNode
            else:
                node = nodeMap[c0]
            curNodes[i] = nodeMap[c0]
            if len(word) == 1:
                curNodes[i].end = True
        
        for i in range(1, t):
            nextNodes = [None]*m
            for j, word in enumerate(wordDict):
                node = curNodes[j]
                if node is None or i >= len(word):
                    continue
                c = word[i]
                if c in node.children:
                    nextNodes[j] = node.children[c]
                else:
                    newNode = Node(c)
                    node.children[c] = newNode
                    nextNodes[j] = newNode
                
                if i == len(word)-1:
                    nextNodes[j].end = True

            curNodes = nextNodes

        def stage(start):
            if start >= n:
                return set()
            c0 = s[start]
            if c0 not in nodeMap:
                return set()
            node = nodeMap[c0]
            validNextIndexes = set()
            if node.end:
                validNextIndexes.add(start+1)
            for i in range(1, t):
                cur = start + i
                if cur == n:
                    return validNextIndexes
                c = s[cur]
                if c not in node.children:
                    return validNextIndexes
                node = node.children[c]
                if node.end:
                    if cur+1 == n:
                        return {n}
                    validNextIndexes.add(cur+1)
            return validNextIndexes
        
        seen = set()
        nextIndexes = {0}
        while nextIndexes:
            newNextIndexes = set()
            for i in nextIndexes:
                if i in seen:
                    continue
                seen.add(i)
                toAdd = stage(i)
                if n in toAdd:
                    return True
                newNextIndexes = newNextIndexes | toAdd
            nextIndexes = newNextIndexes
        
        return False









