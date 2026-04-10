class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = [None]*numCourses
        for i in range(numCourses):
            nodes[i] = Node(i)
        
        for pr in prerequisites:
            child, parent = pr
            nodes[parent].children.append(nodes[child])
        
        allSeen = set()
        for node in nodes:
            if node in allSeen:
                continue
            lineage = set()
            def dfs(cnode, allSeen, lineage):
                if cnode in lineage:
                    return False
                lineage.add(cnode)
                for child in cnode.children:
                    allSeen.add(child)
                    good = dfs(child, allSeen, lineage)
                    if not good:
                        return False
                lineage.remove(cnode)
                return True
            
            valid = dfs(node, allSeen, lineage)
            if not valid:
                return False

            '''
            q = deque([node])
            while q:
                cnode = q.popleft()
                if cnode in localSeen:
                    return False
                localSeen.add(cnode)
                for child in cnode.children:
                    if child in allSeen:
                        continue
                    q.append(child)
            '''
        
        return True

