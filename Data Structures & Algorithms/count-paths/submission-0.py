class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #for each point, we need to know 
        #the number of unique paths you can take from 
        #either going right or down from that

        dp = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]
                

