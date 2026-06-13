class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if len(s) != len(t):
            return False

        for c, a in zip(s, t):
            if c != a:
                return False
        return True
