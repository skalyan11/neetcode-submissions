class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ## binary search done with two pointer in python
        res = r


        while l <= r:
            totalTime = 0
            ## l + r // 2 gives index
            k = (l + r) // 2
            ### check each pile to see total eat time
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res