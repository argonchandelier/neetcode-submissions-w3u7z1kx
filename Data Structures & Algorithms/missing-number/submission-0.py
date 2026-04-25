class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        for i, num in enumerate(nums):
            x = x^i^num
        
        return x