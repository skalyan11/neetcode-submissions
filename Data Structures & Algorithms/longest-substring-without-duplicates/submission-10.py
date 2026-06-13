from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        if not s:
            return 0
        left, right = 0, 0
        n = len(s)
        maxlen = 1
        while right < n:
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])
            maxlen = max(right - left + 1, maxlen)
            right += 1
        
        return maxlen
        
            


                