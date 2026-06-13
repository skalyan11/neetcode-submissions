class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        if not nums:
            return 0
        
        f = {}
        for num in nums:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1
        
        heap = []

        for num, freq in f.items():
            heapq.heappush(heap, (-freq, num))

        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
    
        return res
        
        
