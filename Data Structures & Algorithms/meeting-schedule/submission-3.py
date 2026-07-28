"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        meetings = sorted(intervals, key=lambda x: (x.start, x.end))
        n = len(intervals)
        for i in range(1, n):
            prevMeeting = meetings[i-1]
            meeting = meetings[i]
            if prevMeeting.end > meeting.start:
                return False
        return True
