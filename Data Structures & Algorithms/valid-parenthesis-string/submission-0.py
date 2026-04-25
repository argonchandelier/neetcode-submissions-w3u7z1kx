class Solution:
    def checkValidString(self, s: str) -> bool:
        starPower = 0
        level = 0
        mp = {
            '(': lambda l, s: (l+1, s),
            ')': lambda l, s: (l-1, s),
            '*': lambda l, s: (l-1, s+2)
        }
        for c in s:
            level, starPower = mp[c](level, starPower)
            if level < 0:
                level += 1
                starPower -= 1
                if starPower < 0:
                    return False
        
        return level == 0