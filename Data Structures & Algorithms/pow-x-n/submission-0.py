class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        neg = n < 0
        n = abs(n)
        ans = 1
        for i in range(n):
            ans *= x
        if neg:
            ans = 1/ans
        
        return ans