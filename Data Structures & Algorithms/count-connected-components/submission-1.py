class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        children = [[] for _ in range(n)]

        for v1, v2 in edges:
            children[v1].append(v2)
            children[v2].append(v1)
        
        seen = [False]*n

        nGraphs = 0
        for node, isSeen in enumerate(seen):
            if isSeen:
                continue
            seen[node] = True
            nGraphs += 1
            q = deque([node])
            while q:
                cnode = q.popleft()
                for child in children[cnode]:
                    if seen[child]:
                        continue
                    seen[child] = True
                    q.append(child)

        return nGraphs
