class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # leetcode
        # leet. code
        n = len(s)
        def dfs(i, memo = {}):
            if i == n:
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                m = len(word)
                segment = s[i: i + m]
                if ((i + m) <= n) and segment == word:
                    if dfs(i+m):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
                