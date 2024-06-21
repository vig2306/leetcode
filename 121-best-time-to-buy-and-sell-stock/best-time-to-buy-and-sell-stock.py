class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        maxPrice = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxPrice = max(profit, maxPrice)
                right = right + 1
            
            else:
                left = right
                right = right+1
        
        return maxPrice
                
        