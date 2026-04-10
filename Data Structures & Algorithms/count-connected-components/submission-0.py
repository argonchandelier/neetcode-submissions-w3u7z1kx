class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        children = [[] for _ in range(n)]

        for v1, v2 in edges:
            children[v1].append(v2)
            children[v2].append(v1)
        
        unchecked = {i for i in range(n)}

        nGraphs = 0
        while unchecked != set():
            nGraphs += 1
            node = unchecked.pop()
            q = deque([node])
            while q:
                cnode = q.popleft()
                for child in children[cnode]:
                    if child not in unchecked:
                        continue
                    unchecked.remove(child)
                    q.append(child)

        return nGraphs
        