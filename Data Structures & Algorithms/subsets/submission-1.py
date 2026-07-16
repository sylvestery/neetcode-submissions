class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        output = []

        tmp = []
        def backtrack(curr, idx):
            output.append(curr[:])
            for i in range(idx, len(nums)):
                tmp.append(nums[i])
                backtrack(tmp, i + 1)
                tmp.pop()


        backtrack([], 0)
        return output
        
        