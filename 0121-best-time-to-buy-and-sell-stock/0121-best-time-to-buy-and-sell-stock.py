class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_price = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            curr_profit = prices[i] - min_price
            
            # Update max profit if we found a better one
            if curr_profit > profit:
                profit = curr_profit
                
            # Update min_price OUTSIDE the if statement
            min_price = min(min_price, prices[i])
            
        return profit