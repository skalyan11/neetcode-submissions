class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        left, right = 0, 0
        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                left = right = i
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                if left != i and right != i:
                    return [left + 1, right - 1]
                else:
                    return [i, i]
            elif nums[i] < target:
                l = i + 1
            elif nums[i] > target:
                r = i - 1
        
        return [-1,-1]

