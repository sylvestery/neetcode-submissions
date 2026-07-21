class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals  = sorted(intervals, key=lambda x: x[0])
        prev = sortedIntervals[0]
        result = [prev]
        for i in range(1, len(sortedIntervals)):
            next = sortedIntervals[i]
            prev = result[-1]
            print(prev, next)
            if prev[1] >= next[0]:
                result[-1][1] = max(next[1], prev[1])
            else:
                result.append(next)
            prev = result[-1]
        return result

        