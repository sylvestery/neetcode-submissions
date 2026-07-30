class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #Brute it 
        # i j 0 0 1
        # i j 0 1 ?
        n =  len(nums)
        def dfs(i, memo={}):
            if i >= n:
                return 0
            result = 1
            if i in memo:
                return  memo[i]
            for j in range(i+1, n):
                if nums[i]  < nums [j]:
                    result = max(result,   1 + dfs(j))
            memo[i] =  result
            return memo[i]
        result = 0
        for i in range(n):
            result = max(dfs(i), result)
        return result

        