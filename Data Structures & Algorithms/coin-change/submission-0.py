class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
         """"
         dp[5] = min(dp[4] + 1, 5)


         """
         s = set()
         if not coins:
            return 0
         dp = [amount + 1 for i in range(amount + 1)]
         dp[0] = 0
         for n in range(1, amount + 1):
            for v in coins:
                if n - v >= 0:
                    dp[n] = min(dp[n], 1 + dp[n - v])
        
         return dp[amount] if dp[amount] != amount + 1 else -1
            
            