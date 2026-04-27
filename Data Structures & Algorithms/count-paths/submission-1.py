class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m-1, n-1
        m, n = max(m, n), min(m, n) # For efficiency
        res = 1
        for i in range(1, n+1):
            res = res * (m + i) // i
        return res