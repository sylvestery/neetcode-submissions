class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        # height above sea level.
        # pacific left and up
        # water flow only if height equal or lower.
        # Just for each cell see if the water eventually hits an edge. If the edge is up or left then its pacific. If its bottom or right then its atlantic. 
        # So one option is that we can start from every piece on the edge. Or what I think is better 
        # lets do dumb solution.
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pac = set()
        atl = set()

        def bfs(start, ocean):
            q = deque(start)
            while q:
                r, c = q.popleft()
                ocean.add((r, c))
                for dr, dc in DIRECTIONS:
                    rr = dr + r
                    cc = dc + c
                    if 0 <= rr < m and 0 <= cc < n and (rr, cc) not in ocean:
                        if heights[rr][cc] >= heights[r][c]:
                            q.append((rr, cc))
        result = []
        m = len(heights)
        n = len(heights[0])
        pacific = []
        atlantic = []
        for r in range(m):
            pacific.append((r, 0))
            atlantic.append((r, n-1))
        for c in range(n):
            pacific.append((0, c))
            atlantic.append((m-1, c))
        bfs(pacific, pac)
        bfs(atlantic, atl)
        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        return list(pac.intersection(atl))



