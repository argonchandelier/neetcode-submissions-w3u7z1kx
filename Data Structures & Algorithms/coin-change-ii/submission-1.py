class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        seen = {} # add in (coin(i), amount): num_combos_to_get_here
        def dfs(coini, total):
            if total > amount:
                return 0
            pair = (coini, total)
            if pair in seen:
                return seen[pair]
            if total == amount:
                return 1
            if coini == n:
                return 0
            
            coin = coins[coini]
            #for newTotal in range(total, amount+1, coin):
            #nWays = dfs(coini+1, newTotal)
            nWays = dfs(coini+1, total) + dfs(coini, total+coin)
            seen[pair] = nWays
            return nWays
        
        res = dfs(0, 0)
        return res