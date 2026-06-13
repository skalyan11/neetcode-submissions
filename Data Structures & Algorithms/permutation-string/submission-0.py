class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        s2m = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        n, m = len(s2), len(s1)

        if m > n:
            return False

        for c in s1:
            s1m[c] += 1

        matches = 0
        for i in range(m):
            s2m[s2[i]] += 1

        for i in range(ord('a'), ord('z') + 1):
            if s1m[chr(i)] == s2m[chr(i)]:
                matches += 1

        left = 0
        for right in range(m, n):
            if matches == 26:
                return True

            # add new character
            c = s2[right]
            s2m[c] += 1

            if s2m[c] == s1m[c]:
                matches += 1
            elif s2m[c] == s1m[c] + 1:
                matches -= 1

            # remove old character
            c = s2[left]
            s2m[c] -= 1

            if s2m[c] == s1m[c]:
                matches += 1
            elif s2m[c] == s1m[c] - 1:
                matches -= 1

            left += 1

        return matches == 26