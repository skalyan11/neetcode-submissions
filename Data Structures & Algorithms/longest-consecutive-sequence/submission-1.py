class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ### use a set to find things with O(1)

        if not nums:
            return 0
        
        s = set(nums)
        max_length = 0

        for num in s:
            ### this approach starts at the beginning of each consecutive set
            current_length = 0
            if num - 1 not in s:
                current_num = num
                current_length = 1

                # finds the sequence length by constantly going up
                while current_num + 1 in s:
                    current_num += 1
                    current_length += 1
            max_length = max(max_length, current_length)
        
        return max_length

                
