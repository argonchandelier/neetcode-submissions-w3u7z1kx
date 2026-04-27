class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        prev = [0]*n
        for i, c1 in enumerate(text1):
            mx = 0
            for j, c2 in enumerate(text2):
                pnumNew = mx + 1
                pnum = prev[j]
                mx = max(mx, pnum)
                if c1 == c2:
                    prev[j] = pnumNew
        
        return max(prev)