class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        maxp = max(dp[n - 1], dp[n - 1] * n)
        """

        if not nums:
            return 0
        n = len(nums)
        curr_max = curr_min = result = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]

            if n < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)

            result = max(result, curr_max)
        return result
            
            
