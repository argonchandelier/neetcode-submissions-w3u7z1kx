class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m-1, n-1
        m, n = max(m, n), min(m, n) # For efficiency
        t = m+n
        a, b = 1, 1
        for i in range(m+1, t+1):
            a *= i
        for i in range(1, n+1):
            b *= i
        return a // b