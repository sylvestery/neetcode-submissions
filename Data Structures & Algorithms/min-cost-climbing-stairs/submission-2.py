class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        # i + 1 or i+2 floor
        # cost paid before stepping
        # start at 0 or 1  
        n = len(cost)
        cache = [-1 for _ in range(n)]
        def dfs(i):
            nonlocal cost
            if i >= n:
                return 0
            if cache[i]  != -1:
                return cache[i]
            total = cost[i] + min(dfs(i+1), dfs(i+2))
            cache[i] = total
            return total
        def dp():
            nonlocal cost
            dp = [0 for _ in range(n+1)]
            for i in range(2, n+1):
                dp[i] =  min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            print(dp)
            return dp[-1]

        #return min(dfs(0), dfs(1))
        return dp()
            

