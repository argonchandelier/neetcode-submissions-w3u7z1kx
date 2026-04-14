class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.count = n
        
        def doLoop(p1, p2):
            while p1 >= 0 and p2 < n:
                c1, c2 = s[p1], s[p2]
                if c1 != c2:
                    return
                self.count += 1
                p1, p2 = p1-1, p2+1
        
        for i in range(n):
            doLoop(i-1, i+1)
            doLoop(i, i+1)
        
        return self.count