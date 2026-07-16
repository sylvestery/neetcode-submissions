class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        # Same as last time but just use the current index once.
        result = []
        
        def backtrack(curr, idx, curSum):
            if curSum == target:
                result.append(curr[:])
                return
            if curSum > target:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                nextSum = curSum + candidates[i]
                curr.append(candidates[i])
                backtrack(curr, i+1, nextSum)
                curr.pop()

        backtrack([], 0, 0)
        return result
        