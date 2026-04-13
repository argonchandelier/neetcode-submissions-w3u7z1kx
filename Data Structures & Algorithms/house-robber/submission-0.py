class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        maxims = [0]*l
        maxims[0], maxims[1] = nums[0], nums[1]
        if l > 2:
            maxims[2] = nums[0] + nums[2]
        for i, n in enumerate(nums[3:], start=3):
            maxims[i] = max(maxims[i-2], maxims[i-3]) + n
        
        return max(maxims[-1], maxims[-2])

