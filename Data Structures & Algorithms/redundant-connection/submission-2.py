class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbors = [[] for _ in range(n)]
        for v1, v2 in edges:
            neighbors[v1-1].append(v2-1)
            neighbors[v2-1].append(v1-1)
        
        end = -1
        for i, nbs in enumerate(neighbors):
            if len(nbs) == 1:
                end = i
                break
        if end == -1:
            return edges[-1]
        
        self.rep = -1
        def dfs(node, seen, prev):
            for nb in neighbors[node]:
                print(f"{node = }, {nb = }, {seen = }, {prev = }")
                if nb == prev:
                    continue
                if nb in seen:
                    self.rep = nb
                    return True
                seen.append(nb)
                ret = dfs(nb, seen, node)
                if ret:
                    return True
                seen.pop()
            return False
        seen = [end]
        dfs(end, seen, -1)
        l = -1
        for i, node in enumerate(seen[::-1]):
            if node == self.rep:
                l = i
                break
        
        candidates = seen[-l-1:]

        candPairAndOGIndexes = []
        for i in range(len(candidates)):
            v1, v2 = candidates[i]+1, candidates[(i+1)%len(candidates)]+1
            pair = [min(v1,v2), max(v1,v2)]
            candPairAndOGIndexes.append((pair, edges.index(pair)))

        maxElem = (-1, -1)
        for pair, ogIndex in candPairAndOGIndexes:
            if ogIndex < maxElem[1]:
                continue
            maxElem = (pair, ogIndex)
        
        return maxElem[0]

