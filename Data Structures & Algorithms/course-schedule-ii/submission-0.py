class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nParents = [0]*numCourses
        children = [[] for _ in range(numCourses)]

        for child, parent in prerequisites:
            nParents[child] += 1
            children[parent].append(child)
        
        classes = []
        for i in range(numCourses):
            if nParents[i] == 0:
                classes.append(i)
        
        #print(f"{classes = }\n{nParents = }\n{children = }")
        q = deque(classes.copy())
        while q:
            cur = q.popleft()
            for child in children[cur]:
                nParents[child] -= 1
                if nParents[child] == 0:
                    q.append(child)
                    classes.append(child)

        if set(classes) ^ {i for i in range(numCourses)} != set():
            return []
        return classes
