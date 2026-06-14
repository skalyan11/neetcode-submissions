class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hm = {}
        # key of character map, value appends of sublists
        for word in strs:
            m = [0 for i in range(26)]
            for c in word:
                m[ord(c) - ord('a')] += 1
            tup = tuple(m)
            if tup in hm:
                hm[tup].append(word)
            else:
                hm[tup] = [word]
        return list(hm.values())




                    
        


