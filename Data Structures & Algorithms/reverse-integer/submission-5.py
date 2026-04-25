class Solution:
    def reverse(self, x: int) -> int:
        neg = 1 if x >= 0 else -1
        x *= neg
        s = str(x)
        s = s[::-1]
        x = int(s)*neg
        
        return x if -2**31 <= x < 2**31 else 0