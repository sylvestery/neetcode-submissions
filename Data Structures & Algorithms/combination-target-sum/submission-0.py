class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        # Target integer
        # 2, 2, 5, 9
        # Basically sum of previous input to target.
        # We create subset 
        # We can reuse numbers multiple times.
        # When do we terminate?
        # If we are greater than target go back.
        # If we equal target add the subset?
        tmp = []
        result = []
        def backtrack(curr, idx, curSum):
            if curSum == target:
                result.append(curr[:])
                return
            if curSum > target:
                return
            for i in range(idx, len(nums)):

                tmp.append(nums[i])
                backtrack( tmp, i, curSum + nums[i])
                tmp.pop()
               # backtrack(tmp, i+1, curSum)
                
            return


        backtrack([], 0, 0)
        return result
        