from collections import defaultdict, deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ttimes = [-1]*n
        ttimes[k-1] = 0
        mp = defaultdict(list)
        for (u, v, t) in times:
            mp[u-1].append((v-1, t))
        
        nodes = deque([k-1])
        while nodes:
            node = nodes.popleft()
            T = ttimes[node]
            for (node2, t) in mp[node]:
                tt = t + T
                if ttimes[node2] < 0 or tt < ttimes[node2]:
                    ttimes[node2] = tt
                    nodes.append(node2)
        
        return -1 if -1 in ttimes else max(ttimes)
                

