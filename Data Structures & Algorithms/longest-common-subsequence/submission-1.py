class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Longest common subsequenc means what?
        # How do we brute force it.
        # for every character in the string find all subsequences that exist in both.
        # c -> c
        # ca ca
        # cat c_a_t
        # bat __a_t
        # for every character check the length starting at that character.
        # b -> ___bt
        # b
        # a 
        # t 
        # a -> __a_t 2
        # decision is if match go forward and extend, otherwise
        # increment string 1 or increment string 2. Exhaust all possibility.
        # Basically any point that already matched the string cant be longer than later parts in the string.
        # were gonna brute it first
        m = len(text1)
        n = len(text2)
        def dfs(i, j, memo = {}):
            if i >= m or j >= n:
                return 0
            key = f"{i},{j}"
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            if key in memo:
                return memo[key]
            memo[key] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[key]


        return dfs(0, 0)