charMap = {str(i) for i in range(1,27)}

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        dp = [0]*n
        dp[0] = 1
        dp[-1] = 1
        
        count = 1
        for i in range(1, n):
            c = s[i]
            c2 = s[i-1]
            if c == '0':
                if c2 != '1' and c2 != '2':
                    return 0
            else:
                dp[i] = dp[i-1]
    
            if c2 + c in charMap:
                if n == 2:
                    return 1 if c == '0' else 2
                dp[i] += dp[i-2]

        return dp[-1]