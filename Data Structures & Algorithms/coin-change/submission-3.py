class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        seen = set()
        current = [0]
        
        for ans in range(1, amount+1):
            new = []
            for am in current:
                for c in coins:
                    n = am + c
                    if n > amount or n in seen:
                        continue
                    if n == amount:
                        return ans
                    seen.add(n)
                    new.append(n)
            current = new[:]
            del new
            if not current:
                return -1
        
        return -1
