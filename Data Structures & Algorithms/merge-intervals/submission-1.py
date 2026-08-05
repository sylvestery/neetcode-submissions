class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sInts = sorted(intervals, key=lambda x: x[0])
        prev = sInts[0]
        result = []
        for i in range(1, len(sorted(sInts))):
            if prev[1] >= sInts[i][0]:
                prev[1] = max(sInts[i][1], prev[1])
            else:
                result.append(prev)
                prev = sInts[i]
        return result + [prev]
        