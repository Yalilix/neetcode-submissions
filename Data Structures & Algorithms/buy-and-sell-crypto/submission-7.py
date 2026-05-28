class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        l, r = 0, 1

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l, r = r, r + 1
                continue
            else:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit)
        
        return maxprofit

        
