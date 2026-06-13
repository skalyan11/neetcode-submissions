from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        n = len(s)
        visit = set()

        length = 0
        while right < n:
            if s[right] in visit:
                visit.remove(s[left])
                left += 1
            else:
                visit.add(s[right])
                right += 1
                length = max(length, right - left)
        return length