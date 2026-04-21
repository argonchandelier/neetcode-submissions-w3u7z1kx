class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        first, last = 1, nums[0]
        for ans in range(1, 1000):
            if last >= n-1:
                return ans
            for ind in range(first, last+1):
                num = nums[ind]
                last = max(last, num + ind)
            first = ind+1
            
