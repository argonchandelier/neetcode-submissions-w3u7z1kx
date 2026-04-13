class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
        dp = [[0]*(n-1) for _ in range(2)]
        for i in range(2):
            dp[i][0], dp[i][1] = nums[i+0], nums[i+1]
            dp[i][2] = nums[i] + nums[i+2]
        for j in range(3, n-1):
            for i in range(2):
                dp[i][j] = max(dp[i][j-2], dp[i][j-3]) + nums[(i+j) % n]
        
        print(dp)
        return max(dp[0][-1], dp[0][-2], dp[1][-1], dp[1][-2])
        
