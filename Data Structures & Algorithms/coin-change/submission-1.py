class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ 1 2 3 4 5 6 7 8 9 10 11 12
            1, 2,"""
        ## i = 1, c = 1, 5, 10
        #### 1 = dp[0] + 1
        ### 1 = dp[-4] + 5
        #### 11 = dp[-9] + 10
        dp = [float('inf') for i in range((amount) + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


                
        