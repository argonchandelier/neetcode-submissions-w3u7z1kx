seen = {1: 1, 2: 2}

class Solution:
    def climbStairs(self, n: int) -> int:
        def f(x):
            if x in seen:
                return seen[x]
            seen[x] = f(x-2) + f(x-1)
            return seen[x]

        return f(n)