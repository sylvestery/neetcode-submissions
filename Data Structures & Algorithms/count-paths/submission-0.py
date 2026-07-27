class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # down or right each is a path
        # 0 -> 0 
        # 1, 0 -> 1 # 0, 1 1
        # 2,0 -> 2 #1, 1 3

        def dfs(r, c, memo={} ) -> int:
            if r == (0) and c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            key = f"{r},{c}"
            if key in memo:
                return memo[key]
            memo[key] = dfs(r, c-1) + dfs(r-1, c)
            return memo[key]
        return dfs(m-1, n-1)


        