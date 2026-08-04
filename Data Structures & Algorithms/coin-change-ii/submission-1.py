class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # what is the base case?
        # curr == 0 return 1
        # curr < 0 return 0
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        def dfs(i, amt):
            
            if amt == 0:
                return 1
            if amt < 0:
                return 0
            if i >= len(coins):
                return 0
            if dp[i][amt] != -1:
                return dp[i][amt]
            #if amt in memo:
            #    return 0
            #if amt >= coins[i]:
            dp[i][amt] =dfs(i+1, amt) + dfs(i, amt - coins[i])
            return dp[i][amt]

        return dfs(0, amount)

        