class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        if not digits:
            return []

        ### dg eg fg
        
        res = [""]
        for digit in digits:
            tmp = []
            for curr in res:
                for c in hashmap[digit]:
                    tmp.append(curr + c)
            res = tmp
        return res
                
            