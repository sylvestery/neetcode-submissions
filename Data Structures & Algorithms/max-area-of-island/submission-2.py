class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        maxArea = 0
        m = len(grid)
        n = len(grid[0]) # were assuming well formed.

        visited = set()
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            area = 0
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q:
                r, c = q.popleft()
                area+=1
                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if (0 <= nr < m and 0 <= nc < n) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(bfs(r, c), maxArea)

        return maxArea
        