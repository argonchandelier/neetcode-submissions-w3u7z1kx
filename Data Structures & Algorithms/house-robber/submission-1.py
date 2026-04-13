class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l > 2:
            nums[2] += nums[0]
        for i, n in enumerate(nums):
            if i < 3:
                continue
            nums[i] = max(nums[i-2], nums[i-3]) + n
        
        return max(nums[-1], nums[-2])

