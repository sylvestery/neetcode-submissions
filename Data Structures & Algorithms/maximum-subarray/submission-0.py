class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Brute force
        n = len(nums)
        maxSub = float('-infinity')
        for i in range(n):
            for j in range(i, n):
                sub = nums[i:j+1]
                maxSub = max(maxSub, sum(sub))
                #print(sub, sum(sub))
        return maxSub
        