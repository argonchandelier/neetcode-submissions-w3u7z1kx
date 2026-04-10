class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = [[] for _ in range(n)]
        for v1, v2 in edges:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        
        self.seen = set()
        def dfs(node, prev):
            if node in self.seen:
                return False
            self.seen.add(node)
            for nb in neighbors[node]:
                if nb == prev:
                    continue
                valid = dfs(nb, node)
                if not valid:
                    return False
            return True
        
        valid = dfs(0, -1)
        if not valid:
            return False
        return self.seen ^ {i for i in range(n)} == set()

            