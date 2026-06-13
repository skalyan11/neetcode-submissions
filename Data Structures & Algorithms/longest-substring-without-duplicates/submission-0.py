class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        seen = set()
        first, sec = 0, 0
        count = 0

        #this keeps the window as an invariant
        # everything in the window is legal
        # everything out of the window does not work
        while sec < len(s):
            if s[sec] not in seen:
                seen.add(s[sec])
                count = max(count, sec - first + 1)
                sec += 1
            else:
                seen.remove(s[first])
                first += 1
        return count
            
