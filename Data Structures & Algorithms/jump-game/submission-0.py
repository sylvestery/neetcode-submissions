class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if not nums:
            return False
        end = len(nums) -1
        def dfs(i, dp={}):
            if i == end:
                return True
            #if nums[i] == 0: #if we are not at the end then we have failed.             
            #    return False
            if i in dp:
                return dp[i]
            for jump in range(i+1, min(i + nums[i], end)+1):
                if dfs(jump):
                    dp[i]= True
                    return True
            dp[i] = False
            return False
        return dfs(0)
                
            
            
        #isnt this basically saying for a given value can i jump over 0
        # i pos
        # 0 -> 1 2
 
        