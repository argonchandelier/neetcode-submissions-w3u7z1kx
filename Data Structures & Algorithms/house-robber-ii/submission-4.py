class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
        dp1 = [0]*(n-1)
        dp2 = [0]*(n-1)
        dp1[0], dp1[1], dp1[2] = nums[0], nums[1], nums[0] + nums[2]
        dp2[0], dp2[1], dp2[2] = nums[1], nums[2], nums[1] + nums[3]
        for j in range(3, n-1):
            dp1[j] = max(dp1[j-2], dp1[j-3]) + nums[j % n]
            dp2[j] = max(dp2[j-2], dp2[j-3]) + nums[(1+j) % n]
        
        print(dp1, dp2)
        return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])
        
