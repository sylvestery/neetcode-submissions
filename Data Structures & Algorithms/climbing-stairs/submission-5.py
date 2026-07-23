class Solution:

    def climbStairs(self, n: int) -> int:
        # what does climbing look like.
        # 0 1 2 1 2
        if n <= 2:
            return n
        dp = [None for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]