class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        mx = csum
        for i in range(1, len(nums)):
            csum = max(nums[i], csum + nums[i])
            mx = max(csum, mx)
        return mx