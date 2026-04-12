class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCostMap = [-1]*n
        minCostMap[-1] = cost[-1]
        minCostMap[-2] = cost[-2]
        for x in range(n-3, -1, -1):
            minCostMap[x] = min(minCostMap[x+1], minCostMap[x+2]) + cost[x]
        
        return min(minCostMap[0], minCostMap[1])