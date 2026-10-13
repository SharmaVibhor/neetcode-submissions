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
        intervals.sort(key= lambda interval:interval.start)
        end = -1

        for interval in intervals:
            if(interval.start < end):
                return False
            end = interval.end

        return True

