class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            freq = [0] * 26
        
            for c in word:
                freq[ord(c) - ord('a')] += 1
            
            key = tuple(freq)
            if key not in hm:
                hm[key] = []
            
            hm[key].append(word)
        return list(hm.values())

                    
        


