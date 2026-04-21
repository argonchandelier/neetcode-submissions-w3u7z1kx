class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        mx = csum
        for i in range(1, len(nums)):
            csum += nums[i]
            csum = max(nums[i], csum)
            mx = max(csum, mx)
        return mx