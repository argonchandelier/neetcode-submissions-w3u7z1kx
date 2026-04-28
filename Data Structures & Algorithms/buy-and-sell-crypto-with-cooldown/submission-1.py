class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        d1: hold or don't
        d2: sell hold, keep hold, buy if no hold, still no hold
        d3: sell d1 or d2, buy if no hold or ex, no hold or buy (forced if d2 sell), hold d1 or d2
        d4: sell d1, d2, or d3, buy, no hold or buy, hold
        d5: sell d1-d4, buy, no hold or buy, hold
        ...
        consider: d1 buy, d2 sell profit, d3 wait, d4 buy, d5 sell VS. d4 buy, d5 sell
        dN buy considers highest profit selling dN-2 and before as last sell
        '''
        profCanBuy, profEx, profSell, profHold = 0, 0, 0, 0
        hold = prices[0]

        for i in range(1, len(prices)):
            p = prices[i]
            
            profCanBuy = max(profCanBuy, profEx)
            profEx = profSell
            profSell = profHold + p - hold

            if profCanBuy-p > profHold-hold:
                hold = p
                profHold = profCanBuy
        
        profit = max(profCanBuy, profEx, profSell)
        return profit
