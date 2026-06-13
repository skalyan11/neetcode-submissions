class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            freq = [0 for i in range(26)]
            for c in word:
                index = ord(c) - ord('a')
                freq[index] += 1
            
            freq = tuple(freq)
            if freq not in hm:
                hm[freq] = []
            
            hm[freq].append(word)
        return list(hm.values())





                    
        


