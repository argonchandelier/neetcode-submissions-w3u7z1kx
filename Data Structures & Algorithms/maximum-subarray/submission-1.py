class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        mx = csum
        nums = nums[1:]
        for num in nums:
            csum += num
            if num > csum:
                csum = num
            mx = max(csum, mx)
        return mx