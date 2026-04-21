class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        mx = csum
        for num in nums[1:]:
            csum += num
            if num > csum:
                csum = num
            mx = max(csum, mx)
        return mx