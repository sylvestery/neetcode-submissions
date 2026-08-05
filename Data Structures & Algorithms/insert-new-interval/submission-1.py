class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # specifically we need to get the bounded range rfom the original.
        # this may operate over multiple elements but likely is within just one element.

        n = len(intervals)
        result = []
        i =0
        insertedInterval = newInterval
        # skip intervals
        while i < n and intervals[i][1] < insertedInterval[0]:
            result.append(intervals[i])
            i+=1
        while i < n and intervals[i][0] <= insertedInterval[1]:
            insertedInterval[0] = min(newInterval[0], intervals[i][0])
            insertedInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        result.append(insertedInterval)  
        while i < n:
            result.append(intervals[i])
            i+=1
        return result
        # skip over any that are before since this is presorted.
        #[1, 3] [4, 6] in: [2,5]
        # edges
        #  2 < 3 5 > 4 5 < 6
        # 1,6
        # 