class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sInts = sorted(intervals, key=lambda x: x[0])
        result = [sInts[0]]
        for i in range(1, len(sorted(sInts))):
            if result[-1][1] >= sInts[i][0]:
                result[-1][1] = max(sInts[i][1], result[-1][1])
            else:
                result.append(sInts[i])

        return result 
        