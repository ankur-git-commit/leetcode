class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        curr_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - curr_price)
            curr_price = min(curr_price, prices[i])
        
        return profit

