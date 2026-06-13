class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        

        def rob(h):
            prev1, prev2 = 0, 0
            for m in h:
                curr = max(prev1, m + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(rob(nums[:-1]), rob(nums[1:]))

        
       
