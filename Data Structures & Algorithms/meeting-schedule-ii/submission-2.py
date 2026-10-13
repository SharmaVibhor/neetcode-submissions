"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        res,cur = 0,0
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()

        s,e =0,0

        while s< len(intervals):
            if start[s]<end[e]:
                cur +=1
                s+=1
            else:
                cur-=1
                e+=1
            res = max(res,cur)
        return res
        