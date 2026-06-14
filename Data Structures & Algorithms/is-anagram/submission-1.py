class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key = [0 for i in range(26)]
        if len(s) != len(t):
            return False

        for c, c2 in zip(s, t):
            key[ord(c) - ord('a')] += 1
            key[ord(c2) - ord('a')] -= 1
        

        for i in range(26):
            if key[i] != 0:
                return False
        return True
            
        