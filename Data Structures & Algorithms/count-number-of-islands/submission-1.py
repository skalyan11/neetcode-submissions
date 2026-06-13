from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        m, n = len(grid), len(grid[0])
        queue = deque()
        def bfs(row, col):
            queue.append((row, col))
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]
            while queue:
                row, col = queue.popleft()
                for d in dirs:
                    r = row + d[0]
                    c = col + d[1]
                    if row + d[0] >= 0 and row + d[0] < m and col + d[1] < n and col + d[1] >= 0 and (r, c) not in visit:
                        visit.add((r, c))
                        if grid[r][c] == "1" and (r,c):
                            queue.append((r, c))

        islands = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row, col)
                    islands += 1
        return islands



        