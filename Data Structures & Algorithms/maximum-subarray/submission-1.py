class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Brute force
        n = len(nums)
        maxSub = float('-infinity')
        curSum = 0
        for i in range(0, n):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSub = max(maxSub, curSum)
        return maxSub
        