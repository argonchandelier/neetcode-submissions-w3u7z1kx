from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        to = defaultdict(list)
        for s, e, cost in flights:
            to[s].append((e, cost))
        
        costs = [float('inf')]*n
        costs[src] = 0
        nodes = {src}
        for i in range(k+1):
            new = set()
            newCosts = costs[:]
            for node in nodes:
                for node2, cost in to[node]:
                    c1, c2 = costs[node2], cost+costs[node]
                    if c2 < c1:
                        new.add(node2)
                        newCosts[node2] = c2
            nodes = new
            costs = newCosts
        
        return costs[dst] if costs[dst] < float('inf') else -1

