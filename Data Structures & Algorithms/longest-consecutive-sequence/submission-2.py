class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        maxLen = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            curLen = 1
            while (num + curLen) in numSet:
                curLen+=1
            maxLen = max(curLen, maxLen)
        return maxLen