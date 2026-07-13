class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        n = len(s)
        maxLen = 0
        seen = set()
        st  = 0
        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[st])
                st += 1
            seen.add(c)
            maxLen = max(maxLen, i - st + 1)
        return maxLen