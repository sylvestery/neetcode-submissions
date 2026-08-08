class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # leetcode
        # leet. code
        n = len(s)
        wordSet = set(wordDict)
        def dfs(i, memo = {}):
            if i == n:
                return True
            if i > n:
                return False
            if i in memo:
                return memo[i]
            for j in range(i, n):
                if s[i: j+1] in wordSet:
                    if dfs(j+1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False
        return dfs(0)
                