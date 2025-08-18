class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # curr_price = 0
        # for i in prices:
        #     profit = max(profit, curr_price - i)
        #     curr_price = i
        # return profit


        # # using range
        # if len(prices) < 2:
        #     return 0

        curr_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > curr_price:
                profit = max(profit, prices[i] - curr_price)
            elif prices[i] < curr_price:
                curr_price = prices[i]
        
        return profit

