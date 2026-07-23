class Solution:

    def climbStairs(self, n: int) -> int:
        # what does climbing look like.
        # 0 1 2 1 2
        dp = [None for _ in range(n)]
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if dp[i]:
                return dp[i]
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        return dfs(0)