from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        goal, mod = divmod(sum(nums), 2)
        if mod == 1:
            return False
        self.seen = set()
        def dfs(curSum, curi):
            if curSum == goal:
                return True
            if curSum > goal or curSum in self.seen:
                return False
            self.seen.add(curSum)
            
            for i in range(curi, n):
                result = dfs(curSum + nums[i], i+1)
                if result:
                    return True
            return False
        
        return dfs(0, 0)



