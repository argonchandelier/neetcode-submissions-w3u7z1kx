class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        station, fill = 0, 0
        for i in range(len(gas)-1):
            fill += gas[i] - cost[i]
            if fill < 0:
                station = i+1
                fill = 0
        
        return station