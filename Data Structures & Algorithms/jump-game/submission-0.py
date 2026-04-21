class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if i > mx:
                return False
            mx = max(i+num, mx)
            if mx >= n-1:
                return True
        return True