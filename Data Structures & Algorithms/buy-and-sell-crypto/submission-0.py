class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 1, 5, 6, 7, 1]
        # [1, 9, 8, 7, 10, 11, 12, 13]
        left, right = 0, 1
        end = len(prices)
        maxprofit = 0

        while right < end:
            if prices[right] < prices[left]:
                left = right
            profit = prices[right] - prices[left]
            maxprofit = max(profit, maxprofit)
            right += 1
            
            
            

        return maxprofit
            

    
