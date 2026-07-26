class Solution:
    def rob(self, nums: List[int]) -> int:
        # money in ith house
        # houses in a line
        # ith house neight I-1 i+1
        # so if I rob[i] i-1 and i+1 is not available.
        # top down approach first
        # min(i-1) rob(i+1)
        if not nums:
            return 0
        n = len(nums)

        def dfs(i, memo={}):
            if i >= n or i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i+2) + nums[i], dfs(i+1))
            return memo[i]
            
        return dfs(0)
        