class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        max_profit = 0
        L, R = 0,1

        while R < len(prices):
            max_profit = max(max_profit, prices[R] - prices[L])
            
            if prices[R] < prices[L]:
                L = R
            R += 1
        
        return max_profit