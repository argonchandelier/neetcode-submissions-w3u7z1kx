class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.mx = 1
        self.mxp1, self.mxp2 = 0, 0

        def doLoop(p1, p2, curLen):
            while p1 >= 0 and p2 < n:
                c1, c2 = s[p1], s[p2]
                if c1 != c2:
                    break
                curLen += 2
                if curLen > self.mx:
                    self.mx = curLen
                    self.mxp1, self.mxp2 = p1, p2
                p1, p2 = p1-1, p2+1

        for i in range(n):
            p1, p2 = i-1, i+1
            curLen = 1
            doLoop(i-1, i+1, 3)
            doLoop(i, i+1, 2)

        return s[self.mxp1: self.mxp2+1]        
