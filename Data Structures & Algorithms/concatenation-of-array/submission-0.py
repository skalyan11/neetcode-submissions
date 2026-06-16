class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for i in range(2 * n)]
        for i, num in enumerate(nums):
            res[i] = num
            res[i + n] = num
        return res
