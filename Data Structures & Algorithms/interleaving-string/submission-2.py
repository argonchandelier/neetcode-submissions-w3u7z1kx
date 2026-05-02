class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # It doesn't matter how repeats are split up, m minus n will be the same
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if l1 == 0 or l2 == 0:
            return s1 == s3 or s2 == s3

        s1 += '\n'
        s2 += '\n'
        seen = set()
        def dfs(i1, i2, i3):
            if i3 == l3:
                return True
            t = (i1, i2)
            if t in seen:
                return False
            seen.add(t)
            
            c1, c2, c3 = s1[i1], s2[i2], s3[i3]
            return ((dfs(i1+1, i2, i3+1) if c1 == c3 else False) | (dfs(i1, i2+1, i3+1) if c2 == c3 else False))
            
        return dfs(0, 0, 0)

        
        '''
        def makeDP(s)
            dp = []
            last = s[0]
            count = 1
            for i, c in enumerate(s[1:], start=1):
                if c == last:
                    count += 1
                    continue
                dp.append([last, count])
                count = 1
                last = c
            dp.append([last, count])
            return dp
            
        dp1, dp2, dp3 = makeDP(s1), makeDP(s2), makeDP(s3)

        i1, i2 = 0, 0
        (c1, n1), (c2, n2) = dp1[0], dp2[0]
        for i3, (c3, n3) in enumerate(dp3):
            if c1 == c2:
                if c1 != c3:
                    return False
                if n1+n2 == n3:
                    i1, i2 = i1+1, i2+1
                    (c1, n1), (c2, n2) = dp1[i1], dp2[i2]
                    continue
                if i3+1 == len(dp3):
                    return False
        '''

                
                



