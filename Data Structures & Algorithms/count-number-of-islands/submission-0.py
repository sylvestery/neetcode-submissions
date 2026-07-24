class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        ones =   []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    ones.append((r, c))

        visited = set()
        def bfs(r, c):
            q = deque([(r, c)])

            while  q:
                # new set of ones each time we need to perform edge check
                r, c = q.popleft()
                visited.add((r,c))
                for (dr, dc) in [(-1, 0), (1, 0),  (0, -1), (0, 1)]:
                    rr = r + dr
                    cc = c + dc
                    if (0 <=  rr < m and 0 <= cc < n) and grid[rr][cc]  == '1' and (rr, cc) not in visited:
                        q.append((rr,  cc))

        numIslands =  0
        for (r,c) in ones:
            if (r, c) not in  visited:
                bfs(r,  c)
                numIslands += 1
                         

        return numIslands


