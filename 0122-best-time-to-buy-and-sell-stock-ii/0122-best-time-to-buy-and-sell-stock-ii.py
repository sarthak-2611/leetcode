class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        min_price = prices[0]
        profit = 0
        
        for i in range(n-1):
            if prices[i+1]>prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

            
          
          