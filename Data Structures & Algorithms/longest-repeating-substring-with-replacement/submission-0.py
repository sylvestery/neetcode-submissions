class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute it
        result = 0
        for i in range(len(s)):
            count, maxFreq = defaultdict(int), 0
            for j in range(i, len(s)):
                count[s[j] ] =1 + count[s[j]]
                maxFreq = max(maxFreq, count[s[j]])
                if (j - i + 1) - maxFreq <= k:
                    result = max(result, j-i + 1)
        return result

        