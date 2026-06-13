class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        n = len(nums)
        minsize = float('inf')
        current = 0

        while right < n:
            current += nums[right]
            while current >= target:
                minsize = min(minsize, right - left + 1)
                current -= nums[left]
                left += 1
            right += 1
                
        return 0 if minsize == float('inf') else minsize

            
