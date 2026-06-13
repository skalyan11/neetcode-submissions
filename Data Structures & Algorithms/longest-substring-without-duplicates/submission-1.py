from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first = best = second = 0
        visit = set()
        n = len(s)
        if n == 1:
            return 1
        while second < n:
            while s[second] in visit:
                visit.remove(s[first])
                first += 1
            visit.add(s[second])
            best = max(best, second - first + 1)
            second += 1
        return best


    
