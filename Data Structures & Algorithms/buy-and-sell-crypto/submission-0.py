class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        profit = 0 
        max_profit = 0 

        while r < len(prices):
            profit = prices[r] - prices[l] 
            max_profit = max(max_profit, profit)

            if profit >= 0:
                r += 1
            else:
                l += 1

        return max_profit 


            