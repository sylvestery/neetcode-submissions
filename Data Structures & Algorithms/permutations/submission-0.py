class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        def backtrack(curr, idx):
            if idx == len(nums):
                result.append(curr[:])
                return
            for i in range(idx, len(nums)):
                nums[idx],nums[i ] =nums[i],nums[idx]
                backtrack(nums, idx+1)
                nums[idx],nums[i ] =nums[i],nums[idx]
        backtrack([], 0)
        return result