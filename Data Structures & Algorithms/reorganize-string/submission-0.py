import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        h = {}
        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1

        # Convert dict to a list of (value, key) tuples and heapify
        heap = [(-count, char) for char, count in h.items()]
        heapq.heapify(heap)
        prev_count = 0
        prev_char = ""
        res = ""
        while heap:
            count, char = heapq.heappop(heap)

            res += char

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            count += 1  # because count is negative

            prev_count = count
            prev_char = char

            result = "".join(res)

        return result if len(result) == len(s) else ""