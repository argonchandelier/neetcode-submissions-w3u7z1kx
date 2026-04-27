class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                   dp[i][j] = 1
        
        prev = [0]*n
        for r, row in enumerate(dp):
            mx = 0
            for c, num in enumerate(row):
                if num > 0:
                    pnumNew = mx + 1
                pnum = prev[c]
                mx = max(mx, pnum)
                if num > 0:
                    prev[c] = pnumNew
        
        return max(prev)