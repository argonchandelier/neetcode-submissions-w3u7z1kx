class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)

        p1 = 0
        p2 = 1
        while True:
            if p2 >= n:
                break
            num1 = prices[p1]
            num2 = prices[p2]
            if num1 > num2:
                p1 = p2
                #p2 = p1+1
            else:
                profit = num2-num1
                if profit > maxProfit:
                    maxProfit = profit
            p2 += 1
        
        return maxProfit