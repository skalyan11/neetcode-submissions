class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]

        ##### [5, 4, 3, 2, 2]
        ##### [5, 20, 60, 120, 240]
        ##### [240,48,12,4,2]

        ### [1, 2, 4, 6]
        ###  [1,  1,  2, 8]
        #### [48, 24, 6, 1]
        #### [48, 24, 12, 8]

        last = len(nums) - 2
        for i, num in enumerate(nums):
            if i > 0:
                prefix[i] = prefix[i - 1] * nums[i - 1]
                suffix[last] = suffix[last + 1] * nums[last + 1]
                last -= 1
        
        return [a * b for a, b in zip(prefix, suffix)]
        
            
            
            