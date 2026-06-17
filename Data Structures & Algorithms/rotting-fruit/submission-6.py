class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        rowlen, collen = len(grid), len(grid[0])
        dirs = [[-1,0], [0,-1], [1,0], [0,1]]
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minute = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for ro, co in dirs:
                    nr = r + ro
                    nc = c + co
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in visit and grid[nr][nc] == 1:
                        visit.add((nr, nc))
                        fresh -= 1
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
            minute += 1
        return minute if fresh == 0 else -1
                



