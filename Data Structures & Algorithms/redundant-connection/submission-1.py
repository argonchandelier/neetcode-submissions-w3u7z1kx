class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbors = [[] for _ in range(n)]
        for v1, v2 in edges:
            neighbors[v1-1].append(v2-1)
            neighbors[v2-1].append(v1-1)
        
        end = -1
        print(f"{neighbors = }")
        for i, nbs in enumerate(neighbors):
            if len(nbs) == 1:
                end = i
                break
        if end == -1:
            return edges[-1]
        
        '''
        seen = [False]*n
        seen[end] = True
        q = deque([end, -1])
        snode = -1
        pairs = []
        while q:
            node = q.popleft()
            prev = q.popleft()
            for nb in neighbors[node]: # Dont include backward
                if nb == prev:
                    continue
                pairs.append((min(node, nb), max(node, nb))) #sorted([node, nb]))
                if seen[nb]:
                    snode = nb
                    break
                seen[nb] = True
                q.append(nb)
                q.append(node)
                print(q)
            else:
                continue
            break
        '''
        
        # We know pairs[-1] is valid, now we should see what else is valid
        # (Erase next stuff...)
        # Maybe dfs, then when we hit a seen, we can trace backwards to when it was seen
        self.rep = -1
        def dfs(node, seen, prev):
            for nb in neighbors[node]:
                print(f"{node = }, {nb = }, {seen = }, {prev = }")
                if nb == prev:
                    continue
                if nb in seen: # longer w/o using set?
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
        print(f"{candidates = }\n{end = }\n{l = }, {self.rep = }, {seen = }")

        #return []
        candPairAndOGIndexes = []
        for i in range(len(candidates)):
            v1, v2 = candidates[i]+1, candidates[(i+1)%len(candidates)]+1
            pair = [min(v1,v2), max(v1,v2)]
            print(f"{pair = }, {edges = }")
            candPairAndOGIndexes.append((pair, edges.index(pair)))

        maxElem = (-1, -1)
        for pair, ogIndex in candPairAndOGIndexes:
            if ogIndex < maxElem[1]:
                continue
            if ogIndex == maxElem[1]:
                print("\n\nERROR\n\n")
                continue
            maxElem = (pair, ogIndex)
        
        return maxElem[0]

        '''
        lookfor = pairs[-1][0] if pairs[-1][1] == snode else pairs[-1][1]
        print(f"{pairs = }, {lookfor = }, {snode = }")
        for i, pair in enumerate(pairs[-2::-1]):
            if lookfor in pair:
                candidates = pairs[-i-2:]
                break
        
        print(f"{candidates = }\n{end = }")
        candidates = set(candidates)
        for v1, v2 in edges[::-1]:
            if (v1-1, v2-1) in candidates:
                return [v1, v2]
        '''

        

        


