class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # specifically we need to get the bounded range rfom the original.
        # this may operate over multiple elements but likely is within just one element.
        left_result = []
        right_result =[]
        new_start, new_end = newInterval
        for start, end in intervals:
            if end < new_start:
                left_result.append([start, end])
            elif  start > new_end:
                right_result.append([start,end])
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        return left_result + [[new_start, new_end]] + right_result



        # skip over any that are before since this is presorted.
        #[1, 3] [4, 6] in: [2,5]
        # edges
        #  2 < 3 5 > 4 5 < 6
        # 1,6