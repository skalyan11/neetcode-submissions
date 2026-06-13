from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left = right = 0

        visit = set()

        l = 0
        while right < len(s):
            if s[right] in visit:
                visit.remove(s[left])
                left += 1
            else:
                l = max(l, right - left + 1)
                visit.add(s[right])
                right += 1
        return l
                

                