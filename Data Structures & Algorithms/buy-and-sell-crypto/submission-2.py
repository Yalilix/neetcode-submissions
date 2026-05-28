class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        maxprofit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                curprofit = prices[r] - prices[l] 
                maxprofit = max(maxprofit, curprofit)
            r += 1
        
        return maxprofit

