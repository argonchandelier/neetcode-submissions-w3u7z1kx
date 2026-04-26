mp = {1: True}

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n > 1:
            if n in mp:
                return mp[n]
            s = str(n)
            n = 0
            for c in s:
                n += int(c)**2
            if n in seen:
                for sn in seen:
                    mp[sn] = False
                return False
            seen.add(n)

        for sn in seen:
            mp[sn] = True
        
        return True
            