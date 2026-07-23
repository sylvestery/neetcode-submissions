class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute it
        result = 0
        count = defaultdict(int)
        rangeStart = 0
        maxFreq = 0
        n = len(s)
        for rangeEnd in range(len(s)):
            count[s[rangeEnd]] +=1 
            maxFreq = max(maxFreq, count[s[rangeEnd]])

            while (rangeEnd - rangeStart + 1) - maxFreq > k:
                count[s[rangeStart]] -=1
                rangeStart +=1
            result = max(result, rangeEnd-rangeStart + 1)
            
        return result

        